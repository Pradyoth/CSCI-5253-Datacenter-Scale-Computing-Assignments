# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: add.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='add.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\tadd.proto\"\x1c\n\x04\x41rgs\x12\t\n\x01\x61\x18\x01 \x01(\x03\x12\t\n\x01\x62\x18\x02 \x01(\x03\"\x13\n\x06Output\x12\t\n\x01\x63\x18\x01 \x01(\x03\x32\x1e\n\x03\x41\x64\x64\x12\x17\n\x03Sum\x12\x05.Args\x1a\x07.Output\"\x00\x62\x06proto3')
)




_ARGS = _descriptor.Descriptor(
  name='Args',
  full_name='Args',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='a', full_name='Args.a', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='b', full_name='Args.b', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=13,
  serialized_end=41,
)


_OUTPUT = _descriptor.Descriptor(
  name='Output',
  full_name='Output',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='c', full_name='Output.c', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=43,
  serialized_end=62,
)

DESCRIPTOR.message_types_by_name['Args'] = _ARGS
DESCRIPTOR.message_types_by_name['Output'] = _OUTPUT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Args = _reflection.GeneratedProtocolMessageType('Args', (_message.Message,), {
  'DESCRIPTOR' : _ARGS,
  '__module__' : 'add_pb2'
  # @@protoc_insertion_point(class_scope:Args)
  })
_sym_db.RegisterMessage(Args)

Output = _reflection.GeneratedProtocolMessageType('Output', (_message.Message,), {
  'DESCRIPTOR' : _OUTPUT,
  '__module__' : 'add_pb2'
  # @@protoc_insertion_point(class_scope:Output)
  })
_sym_db.RegisterMessage(Output)



_ADD = _descriptor.ServiceDescriptor(
  name='Add',
  full_name='Add',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=64,
  serialized_end=94,
  methods=[
  _descriptor.MethodDescriptor(
    name='Sum',
    full_name='Add.Sum',
    index=0,
    containing_service=None,
    input_type=_ARGS,
    output_type=_OUTPUT,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_ADD)

DESCRIPTOR.services_by_name['Add'] = _ADD

# @@protoc_insertion_point(module_scope)
