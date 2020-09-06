# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: whoami.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='whoami.proto',
  package='unibit.test',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x0cwhoami.proto\x12\x0bunibit.test\"\t\n\x07Request\")\n\x0bMapEnvEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t\"\x10\n\x02Ip\x12\n\n\x02ip\x18\x01 \x01(\t\"\x7f\n\x08Response\x12\x13\n\x0bserver_name\x18\x01 \x01(\t\x12\"\n\tserver_ip\x18\x02 \x03(\x0b\x32\x0f.unibit.test.Ip\x12\x13\n\x0b\x63lient_conn\x18\x03 \x01(\t\x12%\n\x03\x65nv\x18\x04 \x03(\x0b\x32\x18.unibit.test.MapEnvEntry2A\n\x06Whoami\x12\x37\n\x06Whoami\x12\x14.unibit.test.Request\x1a\x15.unibit.test.Response\"\x00\x62\x06proto3'
)




_REQUEST = _descriptor.Descriptor(
  name='Request',
  full_name='unibit.test.Request',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=29,
  serialized_end=38,
)


_MAPENVENTRY = _descriptor.Descriptor(
  name='MapEnvEntry',
  full_name='unibit.test.MapEnvEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='unibit.test.MapEnvEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='value', full_name='unibit.test.MapEnvEntry.value', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=40,
  serialized_end=81,
)


_IP = _descriptor.Descriptor(
  name='Ip',
  full_name='unibit.test.Ip',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='ip', full_name='unibit.test.Ip.ip', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=83,
  serialized_end=99,
)


_RESPONSE = _descriptor.Descriptor(
  name='Response',
  full_name='unibit.test.Response',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='server_name', full_name='unibit.test.Response.server_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='server_ip', full_name='unibit.test.Response.server_ip', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='client_conn', full_name='unibit.test.Response.client_conn', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='env', full_name='unibit.test.Response.env', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=101,
  serialized_end=228,
)

_RESPONSE.fields_by_name['server_ip'].message_type = _IP
_RESPONSE.fields_by_name['env'].message_type = _MAPENVENTRY
DESCRIPTOR.message_types_by_name['Request'] = _REQUEST
DESCRIPTOR.message_types_by_name['MapEnvEntry'] = _MAPENVENTRY
DESCRIPTOR.message_types_by_name['Ip'] = _IP
DESCRIPTOR.message_types_by_name['Response'] = _RESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Request = _reflection.GeneratedProtocolMessageType('Request', (_message.Message,), {
  'DESCRIPTOR' : _REQUEST,
  '__module__' : 'whoami_pb2'
  # @@protoc_insertion_point(class_scope:unibit.test.Request)
  })
_sym_db.RegisterMessage(Request)

MapEnvEntry = _reflection.GeneratedProtocolMessageType('MapEnvEntry', (_message.Message,), {
  'DESCRIPTOR' : _MAPENVENTRY,
  '__module__' : 'whoami_pb2'
  # @@protoc_insertion_point(class_scope:unibit.test.MapEnvEntry)
  })
_sym_db.RegisterMessage(MapEnvEntry)

Ip = _reflection.GeneratedProtocolMessageType('Ip', (_message.Message,), {
  'DESCRIPTOR' : _IP,
  '__module__' : 'whoami_pb2'
  # @@protoc_insertion_point(class_scope:unibit.test.Ip)
  })
_sym_db.RegisterMessage(Ip)

Response = _reflection.GeneratedProtocolMessageType('Response', (_message.Message,), {
  'DESCRIPTOR' : _RESPONSE,
  '__module__' : 'whoami_pb2'
  # @@protoc_insertion_point(class_scope:unibit.test.Response)
  })
_sym_db.RegisterMessage(Response)



_WHOAMI = _descriptor.ServiceDescriptor(
  name='Whoami',
  full_name='unibit.test.Whoami',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=230,
  serialized_end=295,
  methods=[
  _descriptor.MethodDescriptor(
    name='Whoami',
    full_name='unibit.test.Whoami.Whoami',
    index=0,
    containing_service=None,
    input_type=_REQUEST,
    output_type=_RESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_WHOAMI)

DESCRIPTOR.services_by_name['Whoami'] = _WHOAMI

# @@protoc_insertion_point(module_scope)