# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: yamcs/protobuf/archive/rocksdb_service.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from yamcs.api import annotations_pb2 as yamcs_dot_api_dot_annotations__pb2
from yamcs.api import httpbody_pb2 as yamcs_dot_api_dot_httpbody__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='yamcs/protobuf/archive/rocksdb_service.proto',
  package='yamcs.protobuf.archive',
  syntax='proto2',
  serialized_options=b'\n\022org.yamcs.protobufB\023RocksDbServiceProtoP\001',
  serialized_pb=b'\n,yamcs/protobuf/archive/rocksdb_service.proto\x12\x16yamcs.protobuf.archive\x1a\x1bgoogle/protobuf/empty.proto\x1a\x1byamcs/api/annotations.proto\x1a\x18yamcs/api/httpbody.proto\"d\n\x1eListRocksDbTablespacesResponse\x12\x42\n\x0btablespaces\x18\x01 \x03(\x0b\x32-.yamcs.protobuf.archive.RocksDbTablespaceInfo\"v\n\x15RocksDbTablespaceInfo\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0f\n\x07\x64\x61taDir\x18\x02 \x01(\t\x12>\n\tdatabases\x18\x03 \x03(\x0b\x32+.yamcs.protobuf.archive.RocksDbDatabaseInfo\"^\n\x1cListRocksDbDatabasesResponse\x12>\n\tdatabases\x18\x01 \x03(\x0b\x32+.yamcs.protobuf.archive.RocksDbDatabaseInfo\"J\n\x13RocksDbDatabaseInfo\x12\x12\n\ntablespace\x18\x01 \x01(\t\x12\x0f\n\x07\x64\x61taDir\x18\x02 \x01(\t\x12\x0e\n\x06\x64\x62Path\x18\x03 \x01(\t\"N\n\x15\x42\x61\x63kupDatabaseRequest\x12\x12\n\ntablespace\x18\x01 \x01(\t\x12\x0e\n\x06\x64\x62path\x18\x02 \x01(\t\x12\x11\n\tbackupDir\x18\x03 \x01(\t\"L\n\x16\x43ompactDatabaseRequest\x12\x12\n\ntablespace\x18\x01 \x01(\t\x12\x0e\n\x06\x64\x62path\x18\x02 \x01(\t\x12\x0e\n\x06\x63\x66name\x18\x03 \x01(\t\"=\n\x17\x44\x65scribeDatabaseRequest\x12\x12\n\ntablespace\x18\x01 \x01(\t\x12\x0e\n\x06\x64\x62path\x18\x02 \x01(\t2\xb9\x07\n\nRocksDbApi\x12\x89\x01\n\x0fListTablespaces\x12\x16.google.protobuf.Empty\x1a\x36.yamcs.protobuf.archive.ListRocksDbTablespacesResponse\"&\x8a\x92\x03\"\n /api/archive/rocksdb/tablespaces\x12\xc3\x01\n\x0e\x42\x61\x63kupDatabase\x12-.yamcs.protobuf.archive.BackupDatabaseRequest\x1a\x16.google.protobuf.Empty\"j\x8a\x92\x03\x66\x1a\x32/api/archive/rocksdb/{tablespace}/{dbpath*}:backupb0Tablespace {tablespace} backed up to {backupDir}\x12\x83\x01\n\rListDatabases\x12\x16.google.protobuf.Empty\x1a\x34.yamcs.protobuf.archive.ListRocksDbDatabasesResponse\"$\x8a\x92\x03 \n\x1e/api/archive/rocksdb/databases\x12\xc8\x01\n\x0f\x43ompactDatabase\x12..yamcs.protobuf.archive.CompactDatabaseRequest\x1a\x16.google.protobuf.Empty\"m\x8a\x92\x03i\x1a\x34/api/archive/rocksdb/{tablespace}/{dbpath**}:compactH\x01\x62/Compaction triggered on tablespace {tablespace}\x12\x63\n\x0f\x44\x65scribeRocksDb\x12\x16.google.protobuf.Empty\x1a\x13.yamcs.api.HttpBody\"#\x8a\x92\x03\x1f\n\x1d/api/archive/rocksdb:describe\x12\x95\x01\n\x10\x44\x65scribeDatabase\x12/.yamcs.protobuf.archive.DescribeDatabaseRequest\x1a\x13.yamcs.api.HttpBody\";\x8a\x92\x03\x37\n5/api/archive/rocksdb/{tablespace}/{dbpath**}:describe\x1a\x0b\x82\x80\x01\x07RocksDBB+\n\x12org.yamcs.protobufB\x13RocksDbServiceProtoP\x01'
  ,
  dependencies=[google_dot_protobuf_dot_empty__pb2.DESCRIPTOR,yamcs_dot_api_dot_annotations__pb2.DESCRIPTOR,yamcs_dot_api_dot_httpbody__pb2.DESCRIPTOR,])




_LISTROCKSDBTABLESPACESRESPONSE = _descriptor.Descriptor(
  name='ListRocksDbTablespacesResponse',
  full_name='yamcs.protobuf.archive.ListRocksDbTablespacesResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='tablespaces', full_name='yamcs.protobuf.archive.ListRocksDbTablespacesResponse.tablespaces', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=156,
  serialized_end=256,
)


_ROCKSDBTABLESPACEINFO = _descriptor.Descriptor(
  name='RocksDbTablespaceInfo',
  full_name='yamcs.protobuf.archive.RocksDbTablespaceInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='yamcs.protobuf.archive.RocksDbTablespaceInfo.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='dataDir', full_name='yamcs.protobuf.archive.RocksDbTablespaceInfo.dataDir', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='databases', full_name='yamcs.protobuf.archive.RocksDbTablespaceInfo.databases', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=258,
  serialized_end=376,
)


_LISTROCKSDBDATABASESRESPONSE = _descriptor.Descriptor(
  name='ListRocksDbDatabasesResponse',
  full_name='yamcs.protobuf.archive.ListRocksDbDatabasesResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='databases', full_name='yamcs.protobuf.archive.ListRocksDbDatabasesResponse.databases', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=378,
  serialized_end=472,
)


_ROCKSDBDATABASEINFO = _descriptor.Descriptor(
  name='RocksDbDatabaseInfo',
  full_name='yamcs.protobuf.archive.RocksDbDatabaseInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='tablespace', full_name='yamcs.protobuf.archive.RocksDbDatabaseInfo.tablespace', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='dataDir', full_name='yamcs.protobuf.archive.RocksDbDatabaseInfo.dataDir', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='dbPath', full_name='yamcs.protobuf.archive.RocksDbDatabaseInfo.dbPath', index=2,
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
  serialized_start=474,
  serialized_end=548,
)


_BACKUPDATABASEREQUEST = _descriptor.Descriptor(
  name='BackupDatabaseRequest',
  full_name='yamcs.protobuf.archive.BackupDatabaseRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='tablespace', full_name='yamcs.protobuf.archive.BackupDatabaseRequest.tablespace', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='dbpath', full_name='yamcs.protobuf.archive.BackupDatabaseRequest.dbpath', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='backupDir', full_name='yamcs.protobuf.archive.BackupDatabaseRequest.backupDir', index=2,
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
  serialized_start=550,
  serialized_end=628,
)


_COMPACTDATABASEREQUEST = _descriptor.Descriptor(
  name='CompactDatabaseRequest',
  full_name='yamcs.protobuf.archive.CompactDatabaseRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='tablespace', full_name='yamcs.protobuf.archive.CompactDatabaseRequest.tablespace', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='dbpath', full_name='yamcs.protobuf.archive.CompactDatabaseRequest.dbpath', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='cfname', full_name='yamcs.protobuf.archive.CompactDatabaseRequest.cfname', index=2,
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
  serialized_start=630,
  serialized_end=706,
)


_DESCRIBEDATABASEREQUEST = _descriptor.Descriptor(
  name='DescribeDatabaseRequest',
  full_name='yamcs.protobuf.archive.DescribeDatabaseRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='tablespace', full_name='yamcs.protobuf.archive.DescribeDatabaseRequest.tablespace', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='dbpath', full_name='yamcs.protobuf.archive.DescribeDatabaseRequest.dbpath', index=1,
      number=2, type=9, cpp_type=9, label=1,
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
  serialized_start=708,
  serialized_end=769,
)

_LISTROCKSDBTABLESPACESRESPONSE.fields_by_name['tablespaces'].message_type = _ROCKSDBTABLESPACEINFO
_ROCKSDBTABLESPACEINFO.fields_by_name['databases'].message_type = _ROCKSDBDATABASEINFO
_LISTROCKSDBDATABASESRESPONSE.fields_by_name['databases'].message_type = _ROCKSDBDATABASEINFO
DESCRIPTOR.message_types_by_name['ListRocksDbTablespacesResponse'] = _LISTROCKSDBTABLESPACESRESPONSE
DESCRIPTOR.message_types_by_name['RocksDbTablespaceInfo'] = _ROCKSDBTABLESPACEINFO
DESCRIPTOR.message_types_by_name['ListRocksDbDatabasesResponse'] = _LISTROCKSDBDATABASESRESPONSE
DESCRIPTOR.message_types_by_name['RocksDbDatabaseInfo'] = _ROCKSDBDATABASEINFO
DESCRIPTOR.message_types_by_name['BackupDatabaseRequest'] = _BACKUPDATABASEREQUEST
DESCRIPTOR.message_types_by_name['CompactDatabaseRequest'] = _COMPACTDATABASEREQUEST
DESCRIPTOR.message_types_by_name['DescribeDatabaseRequest'] = _DESCRIBEDATABASEREQUEST
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ListRocksDbTablespacesResponse = _reflection.GeneratedProtocolMessageType('ListRocksDbTablespacesResponse', (_message.Message,), {
  'DESCRIPTOR' : _LISTROCKSDBTABLESPACESRESPONSE,
  '__module__' : 'yamcs.protobuf.archive.rocksdb_service_pb2'
  # @@protoc_insertion_point(class_scope:yamcs.protobuf.archive.ListRocksDbTablespacesResponse)
  })
_sym_db.RegisterMessage(ListRocksDbTablespacesResponse)

RocksDbTablespaceInfo = _reflection.GeneratedProtocolMessageType('RocksDbTablespaceInfo', (_message.Message,), {
  'DESCRIPTOR' : _ROCKSDBTABLESPACEINFO,
  '__module__' : 'yamcs.protobuf.archive.rocksdb_service_pb2'
  # @@protoc_insertion_point(class_scope:yamcs.protobuf.archive.RocksDbTablespaceInfo)
  })
_sym_db.RegisterMessage(RocksDbTablespaceInfo)

ListRocksDbDatabasesResponse = _reflection.GeneratedProtocolMessageType('ListRocksDbDatabasesResponse', (_message.Message,), {
  'DESCRIPTOR' : _LISTROCKSDBDATABASESRESPONSE,
  '__module__' : 'yamcs.protobuf.archive.rocksdb_service_pb2'
  # @@protoc_insertion_point(class_scope:yamcs.protobuf.archive.ListRocksDbDatabasesResponse)
  })
_sym_db.RegisterMessage(ListRocksDbDatabasesResponse)

RocksDbDatabaseInfo = _reflection.GeneratedProtocolMessageType('RocksDbDatabaseInfo', (_message.Message,), {
  'DESCRIPTOR' : _ROCKSDBDATABASEINFO,
  '__module__' : 'yamcs.protobuf.archive.rocksdb_service_pb2'
  # @@protoc_insertion_point(class_scope:yamcs.protobuf.archive.RocksDbDatabaseInfo)
  })
_sym_db.RegisterMessage(RocksDbDatabaseInfo)

BackupDatabaseRequest = _reflection.GeneratedProtocolMessageType('BackupDatabaseRequest', (_message.Message,), {
  'DESCRIPTOR' : _BACKUPDATABASEREQUEST,
  '__module__' : 'yamcs.protobuf.archive.rocksdb_service_pb2'
  # @@protoc_insertion_point(class_scope:yamcs.protobuf.archive.BackupDatabaseRequest)
  })
_sym_db.RegisterMessage(BackupDatabaseRequest)

CompactDatabaseRequest = _reflection.GeneratedProtocolMessageType('CompactDatabaseRequest', (_message.Message,), {
  'DESCRIPTOR' : _COMPACTDATABASEREQUEST,
  '__module__' : 'yamcs.protobuf.archive.rocksdb_service_pb2'
  # @@protoc_insertion_point(class_scope:yamcs.protobuf.archive.CompactDatabaseRequest)
  })
_sym_db.RegisterMessage(CompactDatabaseRequest)

DescribeDatabaseRequest = _reflection.GeneratedProtocolMessageType('DescribeDatabaseRequest', (_message.Message,), {
  'DESCRIPTOR' : _DESCRIBEDATABASEREQUEST,
  '__module__' : 'yamcs.protobuf.archive.rocksdb_service_pb2'
  # @@protoc_insertion_point(class_scope:yamcs.protobuf.archive.DescribeDatabaseRequest)
  })
_sym_db.RegisterMessage(DescribeDatabaseRequest)


DESCRIPTOR._options = None

_ROCKSDBAPI = _descriptor.ServiceDescriptor(
  name='RocksDbApi',
  full_name='yamcs.protobuf.archive.RocksDbApi',
  file=DESCRIPTOR,
  index=0,
  serialized_options=b'\202\200\001\007RocksDB',
  serialized_start=772,
  serialized_end=1725,
  methods=[
  _descriptor.MethodDescriptor(
    name='ListTablespaces',
    full_name='yamcs.protobuf.archive.RocksDbApi.ListTablespaces',
    index=0,
    containing_service=None,
    input_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    output_type=_LISTROCKSDBTABLESPACESRESPONSE,
    serialized_options=b'\212\222\003\"\n /api/archive/rocksdb/tablespaces',
  ),
  _descriptor.MethodDescriptor(
    name='BackupDatabase',
    full_name='yamcs.protobuf.archive.RocksDbApi.BackupDatabase',
    index=1,
    containing_service=None,
    input_type=_BACKUPDATABASEREQUEST,
    output_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    serialized_options=b'\212\222\003f\0322/api/archive/rocksdb/{tablespace}/{dbpath*}:backupb0Tablespace {tablespace} backed up to {backupDir}',
  ),
  _descriptor.MethodDescriptor(
    name='ListDatabases',
    full_name='yamcs.protobuf.archive.RocksDbApi.ListDatabases',
    index=2,
    containing_service=None,
    input_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    output_type=_LISTROCKSDBDATABASESRESPONSE,
    serialized_options=b'\212\222\003 \n\036/api/archive/rocksdb/databases',
  ),
  _descriptor.MethodDescriptor(
    name='CompactDatabase',
    full_name='yamcs.protobuf.archive.RocksDbApi.CompactDatabase',
    index=3,
    containing_service=None,
    input_type=_COMPACTDATABASEREQUEST,
    output_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    serialized_options=b'\212\222\003i\0324/api/archive/rocksdb/{tablespace}/{dbpath**}:compactH\001b/Compaction triggered on tablespace {tablespace}',
  ),
  _descriptor.MethodDescriptor(
    name='DescribeRocksDb',
    full_name='yamcs.protobuf.archive.RocksDbApi.DescribeRocksDb',
    index=4,
    containing_service=None,
    input_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    output_type=yamcs_dot_api_dot_httpbody__pb2._HTTPBODY,
    serialized_options=b'\212\222\003\037\n\035/api/archive/rocksdb:describe',
  ),
  _descriptor.MethodDescriptor(
    name='DescribeDatabase',
    full_name='yamcs.protobuf.archive.RocksDbApi.DescribeDatabase',
    index=5,
    containing_service=None,
    input_type=_DESCRIBEDATABASEREQUEST,
    output_type=yamcs_dot_api_dot_httpbody__pb2._HTTPBODY,
    serialized_options=b'\212\222\0037\n5/api/archive/rocksdb/{tablespace}/{dbpath**}:describe',
  ),
])
_sym_db.RegisterServiceDescriptor(_ROCKSDBAPI)

DESCRIPTOR.services_by_name['RocksDbApi'] = _ROCKSDBAPI

# @@protoc_insertion_point(module_scope)
