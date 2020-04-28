import binascii
import functools
import threading

import six

from yamcs.core.exceptions import YamcsError
from yamcs.core.futures import WebSocketSubscriptionFuture
from yamcs.core.helpers import adapt_name_for_rest, to_isostring
from yamcs.core.subscriptions import WebSocketSubscriptionManager
from yamcs.protobuf import yamcs_pb2
from yamcs.protobuf.alarms import alarms_pb2
from yamcs.protobuf.mdb import mdb_pb2
from yamcs.protobuf.processing import processing_pb2
from yamcs.protobuf.pvalue import pvalue_pb2
from yamcs.protobuf.web import websocket_pb2
from yamcs.tmtc.model import (
    AlarmUpdate,
    Calibrator,
    CommandHistory,
    IssuedCommand,
    MonitoredCommand,
    ParameterData,
    ParameterValue,
    _parse_alarm,
)


class SequenceGenerator(object):
    """Static atomic counter."""

    _counter = 0
    _lock = threading.Lock()

    @classmethod
    def next(cls):
        with cls._lock:
            cls._counter += 1
            return cls._counter


def _wrap_callback_parse_parameter_data(subscription, on_data, message):
    """
    Wraps an (optional) user callback to parse ParameterData
    from a WebSocket data message
    """
    if message.type == message.REPLY:
        data = websocket_pb2.ParameterSubscriptionResponse()
        data.ParseFromString(message.reply.data)
        subscription.subscription_id = data.subscriptionId
    elif message.type == message.DATA and message.data.type == yamcs_pb2.PARAMETER:
        parameter_data = ParameterData(getattr(message.data, "parameterData"))
        subscription._process(parameter_data)
        if on_data:
            on_data(parameter_data)


def _wrap_callback_parse_cmdhist_data(subscription, on_data, message):
    """
    Wraps an (optional) user callback to parse CommandHistoryEntry
    from a WebSocket data message
    """
    if message.type == message.DATA and message.data.type == yamcs_pb2.CMD_HISTORY:
        entry = getattr(message.data, "command")
        rec = subscription._process(entry)
        if on_data:
            on_data(rec)


def _wrap_callback_parse_alarm_data(subscription, on_data, message):
    """
    Wraps an (optional) user callback to parse Alarm data
    from a WebSocket data message
    """
    if message.type == message.DATA and message.data.type == yamcs_pb2.ALARM_DATA:
        proto = getattr(message.data, "alarmData")
        alarm_update = AlarmUpdate(proto)
        subscription._process(alarm_update)
        if on_data:
            on_data(alarm_update)


def _build_named_object_id(parameter):
    """
    Builds a NamedObjectId. This is a bit more complex than it really
    should be. In Python (for convenience) we allow the user to simply address
    entries by their alias via the NAMESPACE/NAME convention. Yamcs is not
    aware of this convention so we decompose it into distinct namespace and
    name fields.
    """
    named_object_id = yamcs_pb2.NamedObjectId()
    if parameter.startswith("/"):
        named_object_id.name = parameter
    else:
        parts = parameter.split("/", 1)
        if len(parts) < 2:
            raise ValueError(
                "Failed to process {}. Use fully-qualified "
                "XTCE names or, alternatively, an alias in "
                "in the format NAMESPACE/NAME".format(parameter)
            )
        named_object_id.namespace = parts[0]
        named_object_id.name = parts[1]
    return named_object_id


def _build_named_object_ids(parameters):
    """Builds a list of NamedObjectId."""
    if isinstance(parameters, str):
        return [_build_named_object_id(parameters)]
    return [_build_named_object_id(parameter) for parameter in parameters]


def _build_value_proto(value):
    proto = yamcs_pb2.Value()
    if isinstance(value, bool):
        proto.type = proto.BOOLEAN
        proto.booleanValue = value
    elif isinstance(value, float):
        proto.type = proto.FLOAT
        proto.floatValue = value
    elif isinstance(value, int) and value > 2147483647:
        proto.type = proto.SINT64
        proto.sint64Value = value
    elif isinstance(value, int):
        proto.type = proto.SINT32
        proto.sint32Value = value
    elif isinstance(value, str):
        proto.type = proto.STRING
        proto.stringValue = value
    else:
        raise YamcsError("Unrecognized type")
    return proto


def _set_range(ar, range, level):
    ar.level = level
    if range[0]:
        ar.minExclusive = range[0]
    if range[1]:
        ar.maxExclusive = range[1]


def _add_alarms(alarm_info, watch, warning, distress, critical, severe, min_violations):
    alarm_info.minViolations = min_violations

    if watch:
        ar = alarm_info.staticAlarmRange.add()
        _set_range(ar, watch, mdb_pb2.WATCH)
    if warning:
        ar = alarm_info.staticAlarmRange.add()
        _set_range(ar, warning, mdb_pb2.WARNING)
    if distress:
        ar = alarm_info.staticAlarmRange.add()
        _set_range(ar, distress, mdb_pb2.DISTRESS)
    if critical:
        ar = alarm_info.staticAlarmRange.add()
        _set_range(ar, critical, mdb_pb2.CRITICAL)
    if severe:
        ar = alarm_info.staticAlarmRange.add()
        _set_range(ar, severe, mdb_pb2.SEVERE)


def _add_calib(calib_info, type, data):
    type = type.lower()
    if type == Calibrator.POLYNOMIAL:
        calib_info.type = mdb_pb2.CalibratorInfo.POLYNOMIAL
        calib_info.polynomialCalibrator.coefficient.extend(data)
    elif type == Calibrator.SPLINE:
        calib_info.type = mdb_pb2.CalibratorInfo.SPLINE
        spline = mdb_pb2.SplineCalibratorInfo()
        for p in data:
            spi = spline.point.add()
            spi.raw = p[0]
            spi.calibrated = p[1]
    else:
        raise YamcsError("Unrecognized type")


class CommandHistorySubscription(WebSocketSubscriptionFuture):
    """
    Local object providing access to command history updates.

    This object buffers all received command history. This is needed
    to stitch together incremental command history events.

    If you expect to receive a lot of command history updates
    you should periodically clear local cache via ``clear_cache()``.
    In future work, we may add automated buffer management within
    configurable watermarks.

    .. warning::
        If command history updates are received for commands
        that are not currently in the local cache, the returned
        information may be incomplete.
    """

    @staticmethod
    def _cache_key(cmd_id):
        """commandId is a tuple. Convert to the equivalent string identifier."""
        return "{}-{}-{}".format(
            cmd_id.generationTime, cmd_id.origin, cmd_id.sequenceNumber
        )

    def __init__(self, manager):
        super(CommandHistorySubscription, self).__init__(manager)
        self._cache = {}

    def clear_cache(self):
        """
        Clears local command history cache.
        """
        self._cache = {}

    def get_command_history(self, issued_command):
        """
        Gets locally cached CommandHistory for the specified command.

        :param .IssuedCommand issued_command: object representing a
                                              previously issued command.
        :rtype: .CommandHistory
        """
        if issued_command.id in self._cache:
            return self._cache[issued_command.id]
        return None

    def _process(self, entry):
        key = self._cache_key(entry.commandId)
        if key in self._cache:
            cmdhist = self._cache[key]
            cmdhist._update(entry.attr)
        else:
            cmdhist = CommandHistory(entry)
            self._cache[key] = cmdhist

        return cmdhist


class ParameterSubscription(WebSocketSubscriptionFuture):
    """
    Local object representing a subscription of zero or more parameters.

    A subscription object stores the last received value of each
    subscribed parameter.
    """

    def __init__(self, manager):
        super(ParameterSubscription, self).__init__(manager)

        self.value_cache = {}
        """Value cache keyed by parameter name."""

        self.delivery_count = 0
        """The number of parameter deliveries."""

        # The actual subscription_id is set async after server reply
        self.subscription_id = -1
        """Subscription number assigned by the server. This is set async,
        so may not be immediately available."""

    def add(self, parameters, abort_on_invalid=True, send_from_cache=True):
        """
        Add one or more parameters to this subscription.

        :param parameters: Parameter(s) to be added
        :type parameters: Union[str, str[]]
        :param bool abort_on_invalid: If ``True`` one invalid parameter
                                      means any other parameter in the
                                      request will also not be added
                                      to the subscription.
        :param bool send_from_cache: If ``True`` the last processed parameter
                                     value is sent from parameter cache.
                                     When ``False`` only newly processed
                                     parameters are received.
        """

        # Verify that we already know our assigned subscription_id
        assert self.subscription_id != -1

        if not parameters:
            return

        options = websocket_pb2.ParameterSubscriptionRequest()
        options.subscriptionId = self.subscription_id
        options.abortOnInvalid = abort_on_invalid
        options.sendFromCache = send_from_cache
        options.id.extend(_build_named_object_ids(parameters))

        self._manager.send("subscribe", options)

    def remove(self, parameters):
        """
        Remove one or more parameters from this subscription.

        :param parameters: Parameter(s) to be removed
        :type parameters: Union[str, str[]]
        """

        # Verify that we already know our assigned subscription_id
        assert self.subscription_id != -1

        if not parameters:
            return

        options = websocket_pb2.ParameterSubscriptionRequest()
        options.subscriptionId = self.subscription_id
        options.id.extend(_build_named_object_ids(parameters))

        self._manager.send("unsubscribe", options)

    def get_value(self, parameter):
        """
        Returns the last value of a specific parameter from local cache.

        :rtype: .ParameterValue
        """
        return self.value_cache[parameter]

    def _process(self, parameter_data):
        self.delivery_count += 1
        for pval in parameter_data.parameters:
            self.value_cache[pval.name] = pval


class CommandConnection(WebSocketSubscriptionFuture):
    """
    Local object providing access to the acknowledgment progress
    of command updates.

    Only commands issued from this object are monitored.
    """

    def __init__(self, manager, client):
        super(CommandConnection, self).__init__(manager)
        self._cmdhist_cache = {}
        self._command_cache = {}
        self._client = client

    def issue(self, command, args=None, dry_run=False, comment=None, verification=None):
        """
        Issue the given command

        :param str command: Either a fully-qualified XTCE name or an alias in the
                            format ``NAMESPACE/NAME``.
        :param dict args: Named arguments (if the command requires these)
        :param bool dry_run: If ``True`` the command is not actually issued. This
                             can be used to test if the server would generate
                             errors when preparing the command (for example
                             because an argument is missing).
        :param str comment: Comment attached to the command.
        :param .VerificationConfig verification: Overrides to the default
                                                 verification handling of this
                                                 command.
        :return: An object providing access to properties of the newly issued
                 command and updated according to command history updates.
        :rtype: .MonitoredCommand
        """
        issued_command = self._client.issue_command(
            command, args, dry_run, comment, verification
        )
        command = MonitoredCommand(issued_command._proto, self._client)

        self._command_cache[command.id] = command

        # It may be that we already received some cmdhist updates
        # before the http response returned.
        if command.id in self._cmdhist_cache:
            cmdhist = self._cmdhist_cache[command.id]
            command._process_cmdhist(cmdhist)

        return command

    def _process(self, entry):
        # TODO would be nice if the server gave this.
        command_id = "{}-{}-{}".format(
            entry.commandId.generationTime,
            entry.commandId.origin,
            entry.commandId.sequenceNumber,
        )

        if command_id in self._cmdhist_cache:
            cmdhist = self._cmdhist_cache[command_id]
            cmdhist._update(entry.attr)
        else:
            cmdhist = CommandHistory(entry)
            self._cmdhist_cache[command_id] = cmdhist

        command = self._command_cache.get(command_id)
        if command:
            command._process_cmdhist(cmdhist)

        return cmdhist


class AlarmSubscription(WebSocketSubscriptionFuture):
    """
    Local object representing an alarm subscription.

    A subscription object stores the currently active
    alarms.
    """

    def __init__(self, manager):
        super(AlarmSubscription, self).__init__(manager)

        self._cache = {}
        """Value cache keyed by alarm name."""

    def get_alarm(self, name):
        """
        Returns the alarm state associated with a specific named
        alarm from local cache.

        :param str name: Fully-qualified name
        :rtype: .Alarm
        """
        return self._cache[name]

    def list_alarms(self):
        """
        Returns a snapshot of all active alarms.

        :rtype: .Alarm[]
        """
        return [self._cache[k] for k in self._cache]

    def _process(self, alarm_update):
        alarm = alarm_update.alarm
        if alarm.processOK and not alarm.triggered and alarm.acknowledged:
            del self._cache[alarm.name]
        else:
            self._cache[alarm.name] = alarm


class ProcessorClient(object):
    """Client object that groups operations linked to a specific processor."""

    def __init__(self, client, instance, processor):
        super(ProcessorClient, self).__init__()
        self._client = client
        self._instance = instance
        self._processor = processor

    def get_parameter_value(self, parameter, from_cache=True, timeout=10):
        """
        Retrieve the current value of the specified parameter.

        :param str parameter: Either a fully-qualified XTCE name or an alias in the
                              format ``NAMESPACE/NAME``.
        :param bool from_cache: If ``False`` this call will block until a
                                fresh value is received on the processor.
                                If ``True`` the server returns the latest
                                value instead (which may be ``None``).
        :param float timeout: The amount of seconds to wait for a fresh value.
                              (ignored if ``from_cache=True``).
        :rtype: .ParameterValue
        """
        params = {
            "fromCache": from_cache,
            "timeout": int(timeout * 1000),
        }
        parameter = adapt_name_for_rest(parameter)
        url = "/processors/{}/{}/parameters{}".format(
            self._instance, self._processor, parameter
        )
        response = self._client.get_proto(url, params=params)
        proto = pvalue_pb2.ParameterValue()
        proto.ParseFromString(response.content)

        # Server returns ParameterValue with only 'id' set if no
        # value existed. Convert this to ``None``.
        if proto.HasField("rawValue") or proto.HasField("engValue"):
            return ParameterValue(proto)
        return None

    def get_parameter_values(self, parameters, from_cache=True, timeout=10):
        """
        Retrieve the current value of the specified parameter.

        :param str[] parameters: List of parameter names. These may be
                                 fully-qualified XTCE name or an alias
                                 in the format ``NAMESPACE/NAME``.
        :param bool from_cache: If ``False`` this call will block until
                                fresh values are received on the processor.
                                If ``True`` the server returns the latest
                                value instead (which may be ``None``).
        :param float timeout: The amount of seconds to wait for a fresh
                              values (ignored if ``from_cache=True``).
        :return: A list that matches the length and order of the requested
                 list of parameters. Each entry contains either the
                 returned parameter value, or ``None``.
        :rtype: .ParameterValue[]
        """
        req = processing_pb2.BatchGetParameterValuesRequest()
        req.id.extend(_build_named_object_ids(parameters))
        req.fromCache = from_cache
        req.timeout = int(timeout * 1000)
        url = "/processors/{}/{}/parameters:batchGet".format(
            self._instance, self._processor
        )
        response = self._client.post_proto(url, data=req.SerializeToString())
        proto = processing_pb2.BatchGetParameterValuesResponse()
        proto.ParseFromString(response.content)

        pvals = []
        for parameter_id in req.id:
            match = None
            for pval in proto.value:
                if pval.id == parameter_id:
                    match = pval
                    break
            pvals.append(ParameterValue(match) if match else None)
        return pvals

    def set_parameter_value(self, parameter, value):
        """
        Sets the value of the specified parameter.

        :param str parameter: Either a fully-qualified XTCE name or an alias in the
                              format ``NAMESPACE/NAME``.
        :param value: The value to set
        """
        parameter = adapt_name_for_rest(parameter)
        url = "/processors/{}/{}/parameters{}".format(
            self._instance, self._processor, parameter
        )
        req = _build_value_proto(value)
        self._client.put_proto(url, data=req.SerializeToString())

    def set_parameter_values(self, values):
        """
        Sets the value of multiple  parameters.

        :param dict values: Values keyed by parameter name. This name can be either
                            a fully-qualified XTCE name or an alias in the format
                            ``NAMESPACE/NAME``.
        """
        req = processing_pb2.BatchSetParameterValuesRequest()
        for key in values:
            item = req.request.add()
            item.id.MergeFrom(_build_named_object_id(key))
            item.value.MergeFrom(_build_value_proto(values[key]))
        url = "/processors/{}/{}/parameters:batchSet".format(
            self._instance, self._processor
        )
        self._client.post_proto(url, data=req.SerializeToString())

    def issue_command(
        self,
        command,
        args=None,
        dry_run=False,
        comment=None,
        verification=None,
        attributes=None,
    ):
        """
        Issue the given command

        :param str command: Either a fully-qualified XTCE name or an alias in the
                            format ``NAMESPACE/NAME``.
        :param dict args: named arguments (if the command requires these)
        :param bool dry_run: If ``True`` the command is not actually issued. This
                             can be used to test if the server would generate
                             errors when preparing the command (for example
                             because an argument is missing).
        :param str comment: Comment attached to the command.
        :param .VerificationConfig verification: Overrides to the default
                                                 verification handling of this
                                                 command.
        :param dict attributes: named extra attributes that will be added to the
                                command history. Might be used by the processor or data
                                links to change the way the command is processed. For
                                example when commanding over a frame link where the
                                COP1 protocol is used, the cop1Bypass attribute can be
                                used to by-pass the COP1 stack (the command will be
                                sent into a so called Type-BD frame)
        :return: An object providing access to properties of the newly issued
                 command.
        :rtype: .IssuedCommand
        """
        req = processing_pb2.IssueCommandRequest()
        req.sequenceNumber = SequenceGenerator.next()
        req.dryRun = dry_run
        if comment:
            req.comment = comment
        if args:
            for key in args:
                assignment = req.assignment.add()
                assignment.name = key

                value = args[key]
                if isinstance(value, six.string_types):
                    # This clause could be remove when we drop py2 (where bytes=str)
                    assignment.value = value
                elif isinstance(value, (bytes, bytearray)):
                    assignment.value = binascii.hexlify(value)
                else:
                    assignment.value = str(value)

        if verification:
            if verification._disable_all:
                req.commandOptions.disableVerifiers = True
            else:
                for verifier in verification._disabled:
                    req.commandOptions.verifierConfig[verifier].disable = True
                for verifier in verification._check_windows:
                    window = verification._check_windows[verifier]
                    if window["start"]:
                        start = int(window["start"] * 1000)
                        req.commandOptions.verifierConfig[
                            verifier
                        ].checkWindow.timeToStartChecking = start
                    if window["stop"]:
                        stop = int(window["stop"] * 1000)
                        req.commandOptions.verifierConfig[
                            verifier
                        ].checkWindow.timeToStopChecking = stop

        if attributes:
            for key in attributes:
                attr = req.attribute.add()
                attr.name = key
                attr.value.MergeFrom(_build_value_proto(attributes[key]))

        command = adapt_name_for_rest(command)
        url = "/processors/{}/{}/commands{}".format(
            self._instance, self._processor, command
        )
        response = self._client.post_proto(url, data=req.SerializeToString())
        proto = processing_pb2.IssueCommandResponse()
        proto.ParseFromString(response.content)
        return IssuedCommand(proto, self)

    def list_alarms(self, start=None, stop=None):
        """
        Lists the active alarms.

        Remark that this does not query the archive. Only active alarms on the
        current processor are returned.

        :param ~datetime.datetime start: Minimum trigger time of the returned alarms
                                         (inclusive)
        :param ~datetime.datetime stop: Maximum trigger time of the returned alarms
                                        (exclusive)
        :rtype: ~collections.Iterable[.Alarm]
        """
        # TODO implement continuation token on server
        params = {"order": "asc"}
        if start is not None:
            params["start"] = to_isostring(start)
        if stop is not None:
            params["stop"] = to_isostring(stop)
        # Server does not do pagination on listings of this resource.
        # Return an iterator anyway for similarity with other API methods
        url = "/processors/{}/{}/alarms".format(self._instance, self._processor)
        response = self._client.get_proto(path=url, params=params)
        message = alarms_pb2.ListAlarmsResponse()
        message.ParseFromString(response.content)
        alarms = getattr(message, "alarms")
        return iter([_parse_alarm(alarm) for alarm in alarms])

    def set_default_calibrator(self, parameter, type, data):
        """
        Apply a calibrator while processing raw values of the specified
        parameter. If there is already a default calibrator associated
        to this parameter, that calibrator gets replaced.

        .. note::

            Contextual calibrators take precedence over the default calibrator
            See :meth:`set_calibrators` for setting contextual calibrators.

        Two types of calibrators can be applied:

        * Polynomial calibrators apply a polynomial expression of the form:
          `y = a + bx + cx^2 + ...`.

          The `data` argument must be an array of floats ``[a, b, c, ...]``.

        * Spline calibrators interpolate the raw value between a set of points
          which represent a linear curve.

          The `data` argument must be an array of ``[x, y]`` points.

        :param str parameter: Either a fully-qualified XTCE name or an alias
                              in the format ``NAMESPACE/NAME``.
        :param str type: One of ``polynomial`` or ``spline``.
        :param data: Calibration definition for the selected type.
        """
        req = mdb_pb2.UpdateParameterRequest()
        req.action = mdb_pb2.UpdateParameterRequest.SET_DEFAULT_CALIBRATOR
        if type:
            _add_calib(req.defaultCalibrator, type, data)

        parameter = adapt_name_for_rest(parameter)
        url = "/mdb/{}/{}/parameters{}".format(
            self._instance, self._processor, parameter
        )
        self._client.patch_proto(url, data=req.SerializeToString())

    def set_calibrators(self, parameter, calibrators):
        """
        Apply an ordered set of calibrators for the specified parameter.
        This replaces existing calibrators (if any).

        Each calibrator may have a context, which indicates when it its
        effects may be applied. Only the first matching calibrator is
        applied.

        A calibrator with context ``None`` is the *default* calibrator.
        There can be only one such calibrator, and is always applied at
        the end when no other contextual calibrator was applicable.

        :param str parameter: Either a fully-qualified XTCE name or an alias
                              in the format ``NAMESPACE/NAME``.
        :param .Calibrator[] calibrators: List of calibrators (either contextual or
                                          not)
        """
        req = mdb_pb2.UpdateParameterRequest()
        req.action = mdb_pb2.UpdateParameterRequest.SET_CALIBRATORS
        for c in calibrators:
            if c.context:
                context_calib = req.contextCalibrator.add()
                context_calib.context = c.context
                calib_info = context_calib.calibrator
            else:
                calib_info = req.defaultCalibrator

            _add_calib(calib_info, c.type, c.data)

        parameter = adapt_name_for_rest(parameter)
        url = "/mdb/{}/{}/parameters{}".format(
            self._instance, self._processor, parameter
        )
        self._client.patch_proto(url, data=req.SerializeToString())

    def clear_calibrators(self, parameter):
        """
        Removes all calibrators for the specified parameter.
        """
        self.set_default_calibrator(parameter, None, None)
        self.set_calibrators(parameter, [])

    def reset_calibrators(self, parameter):
        """
        Reset all calibrators for the specified parameter to their original MDB value.
        """
        req = mdb_pb2.UpdateParameterRequest()
        req.action = mdb_pb2.UpdateParameterRequest.RESET_CALIBRATORS

        parameter = adapt_name_for_rest(parameter)
        url = "/mdb/{}/{}/parameters{}".format(
            self._instance, self._processor, parameter
        )
        self._client.patch_proto(url, data=req.SerializeToString())

    def set_default_alarm_ranges(
        self,
        parameter,
        watch=None,
        warning=None,
        distress=None,
        critical=None,
        severe=None,
        min_violations=1,
    ):
        """
        Generate out-of-limit alarms for a parameter using the specified
        alarm ranges.

        This replaces any previous default alarms on this parameter.

        .. note::

            Contextual range sets take precedence over the default alarm
            ranges. See :meth:`set_alarm_range_sets` for setting contextual
            range sets.

        :param str parameter: Either a fully-qualified XTCE name or an alias
                              in the format ``NAMESPACE/NAME``.
        :param (float,float) watch: Range expressed as a tuple ``(lo, hi)``
                                    where lo and hi are assumed exclusive.
        :param (float,float) warning: Range expressed as a tuple ``(lo, hi)``
                                      where lo and hi are assumed exclusive.
        :param (float,float) distress: Range expressed as a tuple ``(lo, hi)``
                                       where lo and hi are assumed exclusive.
        :param (float,float) critical: Range expressed as a tuple ``(lo, hi)``
                                       where lo and hi are assumed exclusive.
        :param (float,float) severe: Range expressed as a tuple ``(lo, hi)``
                                     where lo and hi are assumed exclusive.
        :param int min_violations: Minimum violations before an alarm is
                                   generated.
        """
        req = mdb_pb2.UpdateParameterRequest()
        req.action = mdb_pb2.UpdateParameterRequest.SET_DEFAULT_ALARMS
        if watch or warning or distress or critical or severe:
            _add_alarms(
                req.defaultAlarm,
                watch,
                warning,
                distress,
                critical,
                severe,
                min_violations,
            )

        parameter = adapt_name_for_rest(parameter)
        url = "/mdb/{}/{}/parameters{}".format(
            self._instance, self._processor, parameter
        )
        self._client.patch_proto(url, data=req.SerializeToString())

    def set_alarm_range_sets(self, parameter, sets):
        """
        Apply an ordered list of alarm range sets for the specified parameter.
        This replaces existing alarm sets (if any).

        Each RangeSet may have a context, which indicates when
        its effects may be applied. Only the first matching set is
        applied.

        A RangeSet with context ``None`` represents the *default* set of
        alarm ranges.  There can be only one such set, and it is always
        applied at the end when no other set of contextual ranges is
        applicable.

        :param str parameter: Either a fully-qualified XTCE name or an alias
                              in the format ``NAMESPACE/NAME``.
        :param .RangeSet[] sets: List of range sets (either contextual or not)
        """
        req = mdb_pb2.UpdateParameterRequest()
        req.action = mdb_pb2.UpdateParameterRequest.SET_ALARMS
        for rs in sets:
            if rs.context:
                context_alarm = req.contextAlarm.add()
                context_alarm.context = rs.context
                alarm_info = context_alarm.alarm
            else:
                alarm_info = req.defaultAlarm

            _add_alarms(
                alarm_info,
                rs.watch,
                rs.warning,
                rs.distress,
                rs.critical,
                rs.severe,
                rs.min_violations,
            )

        parameter = adapt_name_for_rest(parameter)
        url = "/mdb/{}/{}/parameters{}".format(
            self._instance, self._processor, parameter
        )
        self._client.patch_proto(url, data=req.SerializeToString())

    def clear_alarm_ranges(self, parameter):
        """
        Removes all alarm limits for the specified parameter.
        """
        self.set_default_alarm_ranges(parameter)
        self.set_alarm_range_sets(parameter, [])

    def reset_alarm_ranges(self, parameter):
        """
        Reset all alarm limits for the specified parameter to their original MDB value.
        """
        req = mdb_pb2.UpdateParameterRequest()
        req.action = mdb_pb2.UpdateParameterRequest.RESET_ALARMS

        parameter = adapt_name_for_rest(parameter)
        url = "/mdb/{}/{}/parameters{}".format(
            self._instance, self._processor, parameter
        )
        self._client.patch_proto(url, data=req.SerializeToString())

    def acknowledge_alarm(self, alarm, comment=None):
        """
        Acknowledges a specific alarm.

        :param alarm: Alarm instance
        :type alarm: :class:`.Alarm`
        :param str comment: Optional comment to associate with the state
                            change.
        """
        name = adapt_name_for_rest(alarm.name)
        url = "/processors/{}/{}/alarms{}/{}".format(
            self._instance, self._processor, name, alarm.sequence_number
        )
        req = alarms_pb2.EditAlarmRequest()
        req.state = "acknowledged"
        if comment is not None:
            req.comment = comment
        self._client.patch_proto(url, data=req.SerializeToString())

    def unshelve_alarm(self, alarm, comment=None):
        """
        Unshelve an alarm.

        :param alarm: Alarm instance
        :type alarm: :class:`.Alarm`
        :param str comment: Optional comment to associate with the state
                            change.
        """
        name = adapt_name_for_rest(alarm.name)
        url = "/processors/{}/{}/alarms{}/{}".format(
            self._instance, self._processor, name, alarm.sequence_number
        )
        req = alarms_pb2.EditAlarmRequest()
        req.state = "unshelved"
        self._client.patch_proto(url, data=req.SerializeToString())

    def shelve_alarm(self, alarm, comment=None):
        """
        Shelve an alarm.

        :param alarm: Alarm instance
        :type alarm: :class:`.Alarm`
        :param str comment: Optional comment to associate with the state
                            change.
        """
        name = adapt_name_for_rest(alarm.name)
        url = "/processors/{}/{}/alarms{}/{}".format(
            self._instance, self._processor, name, alarm.sequence_number
        )
        req = alarms_pb2.EditAlarmRequest()
        req.state = "shelved"
        if comment is not None:
            req.comment = comment
        self._client.patch_proto(url, data=req.SerializeToString())

    def clear_alarm(self, alarm, comment=None):
        """
        Clear an alarm.

        .. note::
            If the reason that caused the alarm is still present, a new
            alarm instance will be generated.

        :param alarm: Alarm instance
        :type alarm: :class:`.Alarm`
        :param str comment: Optional comment to associate with the state
                            change.
        """
        name = adapt_name_for_rest(alarm.name)
        url = "/processors/{}/{}/alarms{}/{}".format(
            self._instance, self._processor, name, alarm.sequence_number
        )
        req = alarms_pb2.EditAlarmRequest()
        req.state = "cleared"
        if comment is not None:
            req.comment = comment
        self._client.patch_proto(url, data=req.SerializeToString())

    def create_command_connection(self, on_data=None, timeout=60):
        """
        Creates a connection for issuing multiple commands and
        following up on their acknowledgment progress.

        .. note::
            This is a convenience method that merges the functionalities
            of :meth:`create_command_history_subscription` with those of
            :meth:`issue_command`.

        :param on_data: Function that gets called with  :class:`.CommandHistory`
                        updates. Only commands issued from this connection are
                        reported.
        :param timeout: The amount of seconds to wait for the request to
                        complete.
        :type timeout: float
        :return: Future that can be used to manage the background websocket
                 subscription
        :rtype: .CommandConnection
        """
        options = websocket_pb2.CommandHistorySubscriptionRequest()
        options.ignorePastCommands = True

        manager = WebSocketSubscriptionManager(
            self._client, resource="cmdhistory", options=options
        )

        # Represent subscription as a future
        subscription = CommandConnection(manager, self)

        wrapped_callback = functools.partial(
            _wrap_callback_parse_cmdhist_data, subscription, on_data
        )

        manager.open(
            wrapped_callback, instance=self._instance, processor=self._processor
        )

        # Wait until a reply or exception is received
        subscription.reply(timeout=timeout)

        return subscription

    def create_command_history_subscription(self, on_data=None, timeout=60):
        """
        Create a new command history subscription.

        :param on_data: (Optional) Function that gets called with
                        :class:`.CommandHistory` updates.
        :param timeout: The amount of seconds to wait for the request to
                        complete.
        :type timeout: float
        :return: Future that can be used to manage the background websocket
                 subscription
        :rtype: .CommandHistorySubscription
        """
        options = websocket_pb2.CommandHistorySubscriptionRequest()
        options.ignorePastCommands = True

        manager = WebSocketSubscriptionManager(
            self._client, resource="cmdhistory", options=options
        )

        # Represent subscription as a future
        subscription = CommandHistorySubscription(manager)

        wrapped_callback = functools.partial(
            _wrap_callback_parse_cmdhist_data, subscription, on_data
        )

        manager.open(
            wrapped_callback, instance=self._instance, processor=self._processor
        )

        # Wait until a reply or exception is received
        subscription.reply(timeout=timeout)

        return subscription

    def create_parameter_subscription(
        self,
        parameters,
        on_data=None,
        abort_on_invalid=True,
        update_on_expiration=False,
        send_from_cache=True,
        timeout=60,
    ):
        """
        Create a new parameter subscription.

        :param str[] parameters: Parameter names (or aliases).
        :param on_data: (Optional) Function that gets called with
                        :class:`.ParameterData` updates.
        :param bool abort_on_invalid: If ``True`` an error is generated when
                                      invalid parameters are specified.
        :param bool update_on_expiration: If ``True`` an update is received
                                          when a parameter value has become
                                          expired. This update holds the
                                          same value as the last known valid
                                          value, but with status set to
                                          ``EXPIRED``.
        :param bool send_from_cache: If ``True`` the last processed parameter
                                     value is sent from parameter cache.
                                     When ``False`` only newly processed
                                     parameters are received.
        :param float timeout: The amount of seconds to wait for the request
                              to complete.

        :return: A Future that can be used to manage the background websocket
                 subscription.
        :rtype: .ParameterSubscription
        """
        options = websocket_pb2.ParameterSubscriptionRequest()
        options.subscriptionId = -1  # This means 'create a new subscription'
        options.abortOnInvalid = abort_on_invalid
        options.updateOnExpiration = update_on_expiration
        options.sendFromCache = send_from_cache
        options.id.extend(_build_named_object_ids(parameters))

        manager = WebSocketSubscriptionManager(
            self._client, resource="parameter", options=options
        )

        # Represent subscription as a future
        subscription = ParameterSubscription(manager)

        wrapped_callback = functools.partial(
            _wrap_callback_parse_parameter_data, subscription, on_data
        )

        manager.open(
            wrapped_callback, instance=self._instance, processor=self._processor
        )

        # Wait until a reply or exception is received
        subscription.reply(timeout=timeout)

        return subscription

    def create_alarm_subscription(self, on_data=None, timeout=60):
        """
        Create a new alarm subscription.

        :param on_data: (Optional) Function that gets called with
                        :class:`.AlarmUpdate` updates.
        :param float timeout: The amount of seconds to wait for the request
                              to complete.

        :return: A Future that can be used to manage the background websocket
                 subscription.
        :rtype: .AlarmSubscription
        """
        manager = WebSocketSubscriptionManager(self._client, resource="alarms")

        # Represent subscription as a future
        subscription = AlarmSubscription(manager)

        wrapped_callback = functools.partial(
            _wrap_callback_parse_alarm_data, subscription, on_data
        )

        manager.open(
            wrapped_callback, instance=self._instance, processor=self._processor
        )

        # Wait until a reply or exception is received
        subscription.reply(timeout=timeout)

        return subscription

    def set_algorithm(self, parameter, text):
        """
        Change an algorithm text. Can only be peformed on JavaScript or Python
        algorithms.

        :param string text: new algorithm text (as it would appear in excel or XTCE)
        :param str parameter: Either a fully-qualified XTCE name or an alias
                              in the format ``NAMESPACE/NAME``.
        """
        req = mdb_pb2.UpdateAlgorithmRequest()
        req.action = mdb_pb2.UpdateAlgorithmRequest.SET
        req.algorithm.text = text

        parameter = adapt_name_for_rest(parameter)
        url = "/mdb/{}/{}/algorithms{}".format(
            self._instance, self._processor, parameter
        )
        self._client.patch_proto(url, data=req.SerializeToString())

    def reset_algorithm(self, parameter):
        """
        Reset the algorithm text to its original definition from MDB

        :param str parameter: Either a fully-qualified XTCE name or an alias
                              in the format ``NAMESPACE/NAME``.
        """
        req = mdb_pb2.UpdateAlgorithmRequest()
        req.action = mdb_pb2.UpdateAlgorithmRequest.RESET

        parameter = adapt_name_for_rest(parameter)
        url = "/mdb/{}/{}/algorithms{}".format(
            self._instance, self._processor, parameter
        )
        self._client.patch_proto(url, data=req.SerializeToString())
