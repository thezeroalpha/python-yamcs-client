# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: yamcs/protobuf/alarms/alarms.proto

from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from yamcs.protobuf import yamcs_pb2 as yamcs_dot_protobuf_dot_yamcs__pb2
from yamcs.protobuf.mdb import mdb_pb2 as yamcs_dot_protobuf_dot_mdb_dot_mdb__pb2
from yamcs.protobuf.pvalue import pvalue_pb2 as yamcs_dot_protobuf_dot_pvalue_dot_pvalue__pb2
from yamcs.protobuf.events import events_pb2 as yamcs_dot_protobuf_dot_events_dot_events__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='yamcs/protobuf/alarms/alarms.proto',
  package='yamcs.protobuf.alarms',
  syntax='proto2',
  serialized_options=b'\n\022org.yamcs.protobufB\013AlarmsProtoP\001',
  serialized_pb=b'\n\"yamcs/protobuf/alarms/alarms.proto\x12\x15yamcs.protobuf.alarms\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1ayamcs/protobuf/yamcs.proto\x1a\x1cyamcs/protobuf/mdb/mdb.proto\x1a\"yamcs/protobuf/pvalue/pvalue.proto\x1a\"yamcs/protobuf/events/events.proto\"z\n\x0f\x41\x63knowledgeInfo\x12\x16\n\x0e\x61\x63knowledgedBy\x18\x01 \x01(\t\x12\x1a\n\x12\x61\x63knowledgeMessage\x18\x02 \x01(\t\x12\x33\n\x0f\x61\x63knowledgeTime\x18\x05 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\"\x9c\x01\n\nShelveInfo\x12\x11\n\tshelvedBy\x18\x01 \x01(\t\x12\x15\n\rshelveMessage\x18\x02 \x01(\t\x12.\n\nshelveTime\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x34\n\x10shelveExpiration\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\"c\n\tClearInfo\x12\x11\n\tclearedBy\x18\x01 \x01(\t\x12-\n\tclearTime\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x14\n\x0c\x63learMessage\x18\x03 \x01(\t\"\x98\x06\n\tAlarmData\x12.\n\x04type\x18\x01 \x01(\x0e\x32 .yamcs.protobuf.alarms.AlarmType\x12/\n\x0btriggerTime\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12)\n\x02id\x18\x03 \x01(\x0b\x32\x1d.yamcs.protobuf.NamedObjectId\x12\x0e\n\x06seqNum\x18\x04 \x01(\r\x12\x36\n\x08severity\x18\x05 \x01(\x0e\x32$.yamcs.protobuf.alarms.AlarmSeverity\x12\x12\n\nviolations\x18\x06 \x01(\r\x12\r\n\x05\x63ount\x18\x07 \x01(\r\x12?\n\x0f\x61\x63knowledgeInfo\x18\x08 \x01(\x0b\x32&.yamcs.protobuf.alarms.AcknowledgeInfo\x12\x46\n\x10notificationType\x18\t \x01(\x0e\x32,.yamcs.protobuf.alarms.AlarmNotificationType\x12\x42\n\x0fparameterDetail\x18\n \x01(\x0b\x32).yamcs.protobuf.alarms.ParameterAlarmData\x12:\n\x0b\x65ventDetail\x18\x0b \x01(\x0b\x32%.yamcs.protobuf.alarms.EventAlarmData\x12\x10\n\x08latching\x18\x0c \x01(\x08\x12\x11\n\tprocessOK\x18\r \x01(\x08\x12\x11\n\ttriggered\x18\x0e \x01(\x08\x12\x14\n\x0c\x61\x63knowledged\x18\x0f \x01(\x08\x12\x35\n\nshelveInfo\x18\x10 \x01(\x0b\x32!.yamcs.protobuf.alarms.ShelveInfo\x12\x33\n\tclearInfo\x18\x11 \x01(\x0b\x32 .yamcs.protobuf.alarms.ClearInfo\x12.\n\nupdateTime\x18\x12 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x10\n\x08readonly\x18\x13 \x01(\x08\x12\x0f\n\x07pending\x18\x14 \x01(\x08\"\x84\x02\n\x12ParameterAlarmData\x12;\n\x0ctriggerValue\x18\x01 \x01(\x0b\x32%.yamcs.protobuf.pvalue.ParameterValue\x12>\n\x0fmostSevereValue\x18\x02 \x01(\x0b\x32%.yamcs.protobuf.pvalue.ParameterValue\x12;\n\x0c\x63urrentValue\x18\x03 \x01(\x0b\x32%.yamcs.protobuf.pvalue.ParameterValue\x12\x34\n\tparameter\x18\x04 \x01(\x0b\x32!.yamcs.protobuf.mdb.ParameterInfo\"\xaf\x01\n\x0e\x45ventAlarmData\x12\x32\n\x0ctriggerEvent\x18\x01 \x01(\x0b\x32\x1c.yamcs.protobuf.events.Event\x12\x35\n\x0fmostSevereEvent\x18\x02 \x01(\x0b\x32\x1c.yamcs.protobuf.events.Event\x12\x32\n\x0c\x63urrentEvent\x18\x03 \x01(\x0b\x32\x1c.yamcs.protobuf.events.Event*\xc3\x01\n\x15\x41larmNotificationType\x12\n\n\x06\x41\x43TIVE\x10\x01\x12\r\n\tTRIGGERED\x10\x02\x12\x16\n\x12SEVERITY_INCREASED\x10\x03\x12\x11\n\rVALUE_UPDATED\x10\x04\x12\x10\n\x0c\x41\x43KNOWLEDGED\x10\x05\x12\x0b\n\x07\x43LEARED\x10\x06\x12\x07\n\x03RTN\x10\x07\x12\x0b\n\x07SHELVED\x10\x08\x12\r\n\tUNSHELVED\x10\t\x12\t\n\x05RESET\x10\n\x12\x15\n\x11TRIGGERED_PENDING\x10\x0b*%\n\tAlarmType\x12\r\n\tPARAMETER\x10\x01\x12\t\n\x05\x45VENT\x10\x02*O\n\rAlarmSeverity\x12\t\n\x05WATCH\x10\x01\x12\x0b\n\x07WARNING\x10\x02\x12\x0c\n\x08\x44ISTRESS\x10\x03\x12\x0c\n\x08\x43RITICAL\x10\x04\x12\n\n\x06SEVERE\x10\x05\x42#\n\x12org.yamcs.protobufB\x0b\x41larmsProtoP\x01'
  ,
  dependencies=[google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,yamcs_dot_protobuf_dot_yamcs__pb2.DESCRIPTOR,yamcs_dot_protobuf_dot_mdb_dot_mdb__pb2.DESCRIPTOR,yamcs_dot_protobuf_dot_pvalue_dot_pvalue__pb2.DESCRIPTOR,yamcs_dot_protobuf_dot_events_dot_events__pb2.DESCRIPTOR,])

_ALARMNOTIFICATIONTYPE = _descriptor.EnumDescriptor(
  name='AlarmNotificationType',
  full_name='yamcs.protobuf.alarms.AlarmNotificationType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='ACTIVE', index=0, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TRIGGERED', index=1, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SEVERITY_INCREASED', index=2, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='VALUE_UPDATED', index=3, number=4,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ACKNOWLEDGED', index=4, number=5,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CLEARED', index=5, number=6,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='RTN', index=6, number=7,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SHELVED', index=7, number=8,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='UNSHELVED', index=8, number=9,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='RESET', index=9, number=10,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TRIGGERED_PENDING', index=10, number=11,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1845,
  serialized_end=2040,
)
_sym_db.RegisterEnumDescriptor(_ALARMNOTIFICATIONTYPE)

AlarmNotificationType = enum_type_wrapper.EnumTypeWrapper(_ALARMNOTIFICATIONTYPE)
_ALARMTYPE = _descriptor.EnumDescriptor(
  name='AlarmType',
  full_name='yamcs.protobuf.alarms.AlarmType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='PARAMETER', index=0, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='EVENT', index=1, number=2,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=2042,
  serialized_end=2079,
)
_sym_db.RegisterEnumDescriptor(_ALARMTYPE)

AlarmType = enum_type_wrapper.EnumTypeWrapper(_ALARMTYPE)
_ALARMSEVERITY = _descriptor.EnumDescriptor(
  name='AlarmSeverity',
  full_name='yamcs.protobuf.alarms.AlarmSeverity',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='WATCH', index=0, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='WARNING', index=1, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DISTRESS', index=2, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CRITICAL', index=3, number=4,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SEVERE', index=4, number=5,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=2081,
  serialized_end=2160,
)
_sym_db.RegisterEnumDescriptor(_ALARMSEVERITY)

AlarmSeverity = enum_type_wrapper.EnumTypeWrapper(_ALARMSEVERITY)
ACTIVE = 1
TRIGGERED = 2
SEVERITY_INCREASED = 3
VALUE_UPDATED = 4
ACKNOWLEDGED = 5
CLEARED = 6
RTN = 7
SHELVED = 8
UNSHELVED = 9
RESET = 10
TRIGGERED_PENDING = 11
PARAMETER = 1
EVENT = 2
WATCH = 1
WARNING = 2
DISTRESS = 3
CRITICAL = 4
SEVERE = 5



_ACKNOWLEDGEINFO = _descriptor.Descriptor(
  name='AcknowledgeInfo',
  full_name='yamcs.protobuf.alarms.AcknowledgeInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='acknowledgedBy', full_name='yamcs.protobuf.alarms.AcknowledgeInfo.acknowledgedBy', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='acknowledgeMessage', full_name='yamcs.protobuf.alarms.AcknowledgeInfo.acknowledgeMessage', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='acknowledgeTime', full_name='yamcs.protobuf.alarms.AcknowledgeInfo.acknowledgeTime', index=2,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=224,
  serialized_end=346,
)


_SHELVEINFO = _descriptor.Descriptor(
  name='ShelveInfo',
  full_name='yamcs.protobuf.alarms.ShelveInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='shelvedBy', full_name='yamcs.protobuf.alarms.ShelveInfo.shelvedBy', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='shelveMessage', full_name='yamcs.protobuf.alarms.ShelveInfo.shelveMessage', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='shelveTime', full_name='yamcs.protobuf.alarms.ShelveInfo.shelveTime', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='shelveExpiration', full_name='yamcs.protobuf.alarms.ShelveInfo.shelveExpiration', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=349,
  serialized_end=505,
)


_CLEARINFO = _descriptor.Descriptor(
  name='ClearInfo',
  full_name='yamcs.protobuf.alarms.ClearInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='clearedBy', full_name='yamcs.protobuf.alarms.ClearInfo.clearedBy', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='clearTime', full_name='yamcs.protobuf.alarms.ClearInfo.clearTime', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='clearMessage', full_name='yamcs.protobuf.alarms.ClearInfo.clearMessage', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=507,
  serialized_end=606,
)


_ALARMDATA = _descriptor.Descriptor(
  name='AlarmData',
  full_name='yamcs.protobuf.alarms.AlarmData',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='yamcs.protobuf.alarms.AlarmData.type', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='triggerTime', full_name='yamcs.protobuf.alarms.AlarmData.triggerTime', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='id', full_name='yamcs.protobuf.alarms.AlarmData.id', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='seqNum', full_name='yamcs.protobuf.alarms.AlarmData.seqNum', index=3,
      number=4, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='severity', full_name='yamcs.protobuf.alarms.AlarmData.severity', index=4,
      number=5, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='violations', full_name='yamcs.protobuf.alarms.AlarmData.violations', index=5,
      number=6, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='count', full_name='yamcs.protobuf.alarms.AlarmData.count', index=6,
      number=7, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='acknowledgeInfo', full_name='yamcs.protobuf.alarms.AlarmData.acknowledgeInfo', index=7,
      number=8, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='notificationType', full_name='yamcs.protobuf.alarms.AlarmData.notificationType', index=8,
      number=9, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='parameterDetail', full_name='yamcs.protobuf.alarms.AlarmData.parameterDetail', index=9,
      number=10, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='eventDetail', full_name='yamcs.protobuf.alarms.AlarmData.eventDetail', index=10,
      number=11, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='latching', full_name='yamcs.protobuf.alarms.AlarmData.latching', index=11,
      number=12, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='processOK', full_name='yamcs.protobuf.alarms.AlarmData.processOK', index=12,
      number=13, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='triggered', full_name='yamcs.protobuf.alarms.AlarmData.triggered', index=13,
      number=14, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='acknowledged', full_name='yamcs.protobuf.alarms.AlarmData.acknowledged', index=14,
      number=15, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='shelveInfo', full_name='yamcs.protobuf.alarms.AlarmData.shelveInfo', index=15,
      number=16, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='clearInfo', full_name='yamcs.protobuf.alarms.AlarmData.clearInfo', index=16,
      number=17, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='updateTime', full_name='yamcs.protobuf.alarms.AlarmData.updateTime', index=17,
      number=18, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='readonly', full_name='yamcs.protobuf.alarms.AlarmData.readonly', index=18,
      number=19, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='pending', full_name='yamcs.protobuf.alarms.AlarmData.pending', index=19,
      number=20, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=609,
  serialized_end=1401,
)


_PARAMETERALARMDATA = _descriptor.Descriptor(
  name='ParameterAlarmData',
  full_name='yamcs.protobuf.alarms.ParameterAlarmData',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='triggerValue', full_name='yamcs.protobuf.alarms.ParameterAlarmData.triggerValue', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='mostSevereValue', full_name='yamcs.protobuf.alarms.ParameterAlarmData.mostSevereValue', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='currentValue', full_name='yamcs.protobuf.alarms.ParameterAlarmData.currentValue', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='parameter', full_name='yamcs.protobuf.alarms.ParameterAlarmData.parameter', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1404,
  serialized_end=1664,
)


_EVENTALARMDATA = _descriptor.Descriptor(
  name='EventAlarmData',
  full_name='yamcs.protobuf.alarms.EventAlarmData',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='triggerEvent', full_name='yamcs.protobuf.alarms.EventAlarmData.triggerEvent', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='mostSevereEvent', full_name='yamcs.protobuf.alarms.EventAlarmData.mostSevereEvent', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='currentEvent', full_name='yamcs.protobuf.alarms.EventAlarmData.currentEvent', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1667,
  serialized_end=1842,
)

_ACKNOWLEDGEINFO.fields_by_name['acknowledgeTime'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_SHELVEINFO.fields_by_name['shelveTime'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_SHELVEINFO.fields_by_name['shelveExpiration'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_CLEARINFO.fields_by_name['clearTime'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_ALARMDATA.fields_by_name['type'].enum_type = _ALARMTYPE
_ALARMDATA.fields_by_name['triggerTime'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_ALARMDATA.fields_by_name['id'].message_type = yamcs_dot_protobuf_dot_yamcs__pb2._NAMEDOBJECTID
_ALARMDATA.fields_by_name['severity'].enum_type = _ALARMSEVERITY
_ALARMDATA.fields_by_name['acknowledgeInfo'].message_type = _ACKNOWLEDGEINFO
_ALARMDATA.fields_by_name['notificationType'].enum_type = _ALARMNOTIFICATIONTYPE
_ALARMDATA.fields_by_name['parameterDetail'].message_type = _PARAMETERALARMDATA
_ALARMDATA.fields_by_name['eventDetail'].message_type = _EVENTALARMDATA
_ALARMDATA.fields_by_name['shelveInfo'].message_type = _SHELVEINFO
_ALARMDATA.fields_by_name['clearInfo'].message_type = _CLEARINFO
_ALARMDATA.fields_by_name['updateTime'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_PARAMETERALARMDATA.fields_by_name['triggerValue'].message_type = yamcs_dot_protobuf_dot_pvalue_dot_pvalue__pb2._PARAMETERVALUE
_PARAMETERALARMDATA.fields_by_name['mostSevereValue'].message_type = yamcs_dot_protobuf_dot_pvalue_dot_pvalue__pb2._PARAMETERVALUE
_PARAMETERALARMDATA.fields_by_name['currentValue'].message_type = yamcs_dot_protobuf_dot_pvalue_dot_pvalue__pb2._PARAMETERVALUE
_PARAMETERALARMDATA.fields_by_name['parameter'].message_type = yamcs_dot_protobuf_dot_mdb_dot_mdb__pb2._PARAMETERINFO
_EVENTALARMDATA.fields_by_name['triggerEvent'].message_type = yamcs_dot_protobuf_dot_events_dot_events__pb2._EVENT
_EVENTALARMDATA.fields_by_name['mostSevereEvent'].message_type = yamcs_dot_protobuf_dot_events_dot_events__pb2._EVENT
_EVENTALARMDATA.fields_by_name['currentEvent'].message_type = yamcs_dot_protobuf_dot_events_dot_events__pb2._EVENT
DESCRIPTOR.message_types_by_name['AcknowledgeInfo'] = _ACKNOWLEDGEINFO
DESCRIPTOR.message_types_by_name['ShelveInfo'] = _SHELVEINFO
DESCRIPTOR.message_types_by_name['ClearInfo'] = _CLEARINFO
DESCRIPTOR.message_types_by_name['AlarmData'] = _ALARMDATA
DESCRIPTOR.message_types_by_name['ParameterAlarmData'] = _PARAMETERALARMDATA
DESCRIPTOR.message_types_by_name['EventAlarmData'] = _EVENTALARMDATA
DESCRIPTOR.enum_types_by_name['AlarmNotificationType'] = _ALARMNOTIFICATIONTYPE
DESCRIPTOR.enum_types_by_name['AlarmType'] = _ALARMTYPE
DESCRIPTOR.enum_types_by_name['AlarmSeverity'] = _ALARMSEVERITY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

AcknowledgeInfo = _reflection.GeneratedProtocolMessageType('AcknowledgeInfo', (_message.Message,), {
  'DESCRIPTOR' : _ACKNOWLEDGEINFO,
  '__module__' : 'yamcs.protobuf.alarms.alarms_pb2'
  # @@protoc_insertion_point(class_scope:yamcs.protobuf.alarms.AcknowledgeInfo)
  })
_sym_db.RegisterMessage(AcknowledgeInfo)

ShelveInfo = _reflection.GeneratedProtocolMessageType('ShelveInfo', (_message.Message,), {
  'DESCRIPTOR' : _SHELVEINFO,
  '__module__' : 'yamcs.protobuf.alarms.alarms_pb2'
  # @@protoc_insertion_point(class_scope:yamcs.protobuf.alarms.ShelveInfo)
  })
_sym_db.RegisterMessage(ShelveInfo)

ClearInfo = _reflection.GeneratedProtocolMessageType('ClearInfo', (_message.Message,), {
  'DESCRIPTOR' : _CLEARINFO,
  '__module__' : 'yamcs.protobuf.alarms.alarms_pb2'
  # @@protoc_insertion_point(class_scope:yamcs.protobuf.alarms.ClearInfo)
  })
_sym_db.RegisterMessage(ClearInfo)

AlarmData = _reflection.GeneratedProtocolMessageType('AlarmData', (_message.Message,), {
  'DESCRIPTOR' : _ALARMDATA,
  '__module__' : 'yamcs.protobuf.alarms.alarms_pb2'
  # @@protoc_insertion_point(class_scope:yamcs.protobuf.alarms.AlarmData)
  })
_sym_db.RegisterMessage(AlarmData)

ParameterAlarmData = _reflection.GeneratedProtocolMessageType('ParameterAlarmData', (_message.Message,), {
  'DESCRIPTOR' : _PARAMETERALARMDATA,
  '__module__' : 'yamcs.protobuf.alarms.alarms_pb2'
  # @@protoc_insertion_point(class_scope:yamcs.protobuf.alarms.ParameterAlarmData)
  })
_sym_db.RegisterMessage(ParameterAlarmData)

EventAlarmData = _reflection.GeneratedProtocolMessageType('EventAlarmData', (_message.Message,), {
  'DESCRIPTOR' : _EVENTALARMDATA,
  '__module__' : 'yamcs.protobuf.alarms.alarms_pb2'
  # @@protoc_insertion_point(class_scope:yamcs.protobuf.alarms.EventAlarmData)
  })
_sym_db.RegisterMessage(EventAlarmData)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
