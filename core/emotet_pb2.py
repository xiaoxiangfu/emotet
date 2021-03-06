# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: emotet.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='emotet.proto',
  package='',
  syntax='proto2',
  serialized_pb=_b('\n\x0c\x65motet.proto\"\x92\x01\n\x17RegistrationRequestBody\x12\x0f\n\x07\x63ommand\x18\x01 \x02(\x05\x12\r\n\x05\x62otId\x18\x02 \x02(\t\x12\x11\n\tosVersion\x18\x03 \x02(\x07\x12\r\n\x05\x63rc32\x18\x04 \x02(\x07\x12\x10\n\x08procList\x18\x05 \x02(\t\x12\x12\n\nmoduleList\x18\x06 \x02(\x0c\x12\x0f\n\x07unknown\x18\x07 \x02(\t\"4\n\x13RegistrationRequest\x12\x0f\n\x07\x63ommand\x18\x01 \x02(\x05\x12\x0c\n\x04\x64\x61ta\x18\x02 \x01(\x0c\"$\n\x06Module\x12\x0c\n\x04type\x18\x01 \x02(\x05\x12\x0c\n\x04\x64\x61ta\x18\x02 \x02(\x0c\"B\n\x14RegistrationResponse\x12\x0c\n\x04\x64\x61ta\x18\x01 \x01(\x0c\x12\x0f\n\x07modules\x18\x02 \x01(\x0c\x12\x0b\n\x03unk\x18\x03 \x01(\x0c\"M\n\x0fSpamRequestBody\x12\x0f\n\x07magicId\x18\x01 \x02(\x05\x12\r\n\x05\x62otId\x18\x02 \x02(\t\x12\x0c\n\x04unk1\x18\x03 \x02(\x0c\x12\x0c\n\x04unk2\x18\x04 \x02(\x0c')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_REGISTRATIONREQUESTBODY = _descriptor.Descriptor(
  name='RegistrationRequestBody',
  full_name='RegistrationRequestBody',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='command', full_name='RegistrationRequestBody.command', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='botId', full_name='RegistrationRequestBody.botId', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='osVersion', full_name='RegistrationRequestBody.osVersion', index=2,
      number=3, type=7, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='crc32', full_name='RegistrationRequestBody.crc32', index=3,
      number=4, type=7, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='procList', full_name='RegistrationRequestBody.procList', index=4,
      number=5, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='moduleList', full_name='RegistrationRequestBody.moduleList', index=5,
      number=6, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='unknown', full_name='RegistrationRequestBody.unknown', index=6,
      number=7, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=17,
  serialized_end=163,
)


_REGISTRATIONREQUEST = _descriptor.Descriptor(
  name='RegistrationRequest',
  full_name='RegistrationRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='command', full_name='RegistrationRequest.command', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='data', full_name='RegistrationRequest.data', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=165,
  serialized_end=217,
)


_MODULE = _descriptor.Descriptor(
  name='Module',
  full_name='Module',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='Module.type', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='data', full_name='Module.data', index=1,
      number=2, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=219,
  serialized_end=255,
)


_REGISTRATIONRESPONSE = _descriptor.Descriptor(
  name='RegistrationResponse',
  full_name='RegistrationResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='data', full_name='RegistrationResponse.data', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='modules', full_name='RegistrationResponse.modules', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='unk', full_name='RegistrationResponse.unk', index=2,
      number=3, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=257,
  serialized_end=323,
)


_SPAMREQUESTBODY = _descriptor.Descriptor(
  name='SpamRequestBody',
  full_name='SpamRequestBody',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='magicId', full_name='SpamRequestBody.magicId', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='botId', full_name='SpamRequestBody.botId', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='unk1', full_name='SpamRequestBody.unk1', index=2,
      number=3, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='unk2', full_name='SpamRequestBody.unk2', index=3,
      number=4, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=325,
  serialized_end=402,
)

DESCRIPTOR.message_types_by_name['RegistrationRequestBody'] = _REGISTRATIONREQUESTBODY
DESCRIPTOR.message_types_by_name['RegistrationRequest'] = _REGISTRATIONREQUEST
DESCRIPTOR.message_types_by_name['Module'] = _MODULE
DESCRIPTOR.message_types_by_name['RegistrationResponse'] = _REGISTRATIONRESPONSE
DESCRIPTOR.message_types_by_name['SpamRequestBody'] = _SPAMREQUESTBODY

RegistrationRequestBody = _reflection.GeneratedProtocolMessageType('RegistrationRequestBody', (_message.Message,), dict(
  DESCRIPTOR = _REGISTRATIONREQUESTBODY,
  __module__ = 'emotet_pb2'
  # @@protoc_insertion_point(class_scope:RegistrationRequestBody)
  ))
_sym_db.RegisterMessage(RegistrationRequestBody)

RegistrationRequest = _reflection.GeneratedProtocolMessageType('RegistrationRequest', (_message.Message,), dict(
  DESCRIPTOR = _REGISTRATIONREQUEST,
  __module__ = 'emotet_pb2'
  # @@protoc_insertion_point(class_scope:RegistrationRequest)
  ))
_sym_db.RegisterMessage(RegistrationRequest)

Module = _reflection.GeneratedProtocolMessageType('Module', (_message.Message,), dict(
  DESCRIPTOR = _MODULE,
  __module__ = 'emotet_pb2'
  # @@protoc_insertion_point(class_scope:Module)
  ))
_sym_db.RegisterMessage(Module)

RegistrationResponse = _reflection.GeneratedProtocolMessageType('RegistrationResponse', (_message.Message,), dict(
  DESCRIPTOR = _REGISTRATIONRESPONSE,
  __module__ = 'emotet_pb2'
  # @@protoc_insertion_point(class_scope:RegistrationResponse)
  ))
_sym_db.RegisterMessage(RegistrationResponse)

SpamRequestBody = _reflection.GeneratedProtocolMessageType('SpamRequestBody', (_message.Message,), dict(
  DESCRIPTOR = _SPAMREQUESTBODY,
  __module__ = 'emotet_pb2'
  # @@protoc_insertion_point(class_scope:SpamRequestBody)
  ))
_sym_db.RegisterMessage(SpamRequestBody)


# @@protoc_insertion_point(module_scope)
