# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: communication.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x13\x63ommunication.proto\"1\n\x0eMessageRequest\x12\x0e\n\x06sender\x18\x01 \x01(\t\x12\x0f\n\x07message\x18\x02 \x01(\t\"\"\n\x0fMessageResponse\x12\x0f\n\x07message\x18\x01 \x01(\t2A\n\rCommunication\x12\x30\n\x0bSendMessage\x12\x0f.MessageRequest\x1a\x10.MessageResponseB\x19\xaa\x02\x16\x45ventManagementServiceb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'communication_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\252\002\026EventManagementService'
  _globals['_MESSAGEREQUEST']._serialized_start=23
  _globals['_MESSAGEREQUEST']._serialized_end=72
  _globals['_MESSAGERESPONSE']._serialized_start=74
  _globals['_MESSAGERESPONSE']._serialized_end=108
  _globals['_COMMUNICATION']._serialized_start=110
  _globals['_COMMUNICATION']._serialized_end=175
# @@protoc_insertion_point(module_scope)
