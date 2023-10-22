# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: eventManager.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x12\x65ventManager.proto\"\x07\n\x05\x45mpty\"\x1a\n\x0cGetByEventId\x12\n\n\x02id\x18\x01 \x01(\x05\"[\n\x0c\x45ventDetails\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x0c\n\x04\x64\x61te\x18\x03 \x01(\t\x12\x10\n\x08location\x18\x04 \x01(\t\x12\x11\n\tdressCode\x18\x05 \x01(\t\"&\n\x06\x45vents\x12\x1c\n\x05items\x18\x01 \x03(\x0b\x32\r.EventDetails\".\n\x0e\x43reateNewEvent\x12\x1c\n\x05\x65vent\x18\x01 \x01(\x0b\x32\r.EventDetails\"+\n\x0bUpdateEvent\x12\x1c\n\x05\x65vent\x18\x01 \x01(\x0b\x32\r.EventDetails\" \n\x12\x44\x65leteEventRequest\x12\n\n\x02id\x18\x01 \x01(\x05\"(\n\x13\x44\x65leteEventResponse\x12\x11\n\tisDeleted\x18\x01 \x01(\x08\x32\x92\x02\n\x13\x45ventManagerService\x12$\n\x11GetEventListAsync\x12\x06.Empty\x1a\x07.Events\x12\x31\n\x11GetEventByIdAsync\x12\r.GetByEventId\x1a\r.EventDetails\x12\x32\n\x10\x43reateEventAsync\x12\x0f.CreateNewEvent\x1a\r.EventDetails\x12/\n\x10UpdateEventAsync\x12\x0c.UpdateEvent\x1a\r.EventDetails\x12=\n\x10\x44\x65leteEventAsync\x12\x13.DeleteEventRequest\x1a\x14.DeleteEventResponseB \xaa\x02\x1d\x45ventManagementService.Protosb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'eventManager_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\252\002\035EventManagementService.Protos'
  _globals['_EMPTY']._serialized_start=22
  _globals['_EMPTY']._serialized_end=29
  _globals['_GETBYEVENTID']._serialized_start=31
  _globals['_GETBYEVENTID']._serialized_end=57
  _globals['_EVENTDETAILS']._serialized_start=59
  _globals['_EVENTDETAILS']._serialized_end=150
  _globals['_EVENTS']._serialized_start=152
  _globals['_EVENTS']._serialized_end=190
  _globals['_CREATENEWEVENT']._serialized_start=192
  _globals['_CREATENEWEVENT']._serialized_end=238
  _globals['_UPDATEEVENT']._serialized_start=240
  _globals['_UPDATEEVENT']._serialized_end=283
  _globals['_DELETEEVENTREQUEST']._serialized_start=285
  _globals['_DELETEEVENTREQUEST']._serialized_end=317
  _globals['_DELETEEVENTRESPONSE']._serialized_start=319
  _globals['_DELETEEVENTRESPONSE']._serialized_end=359
  _globals['_EVENTMANAGERSERVICE']._serialized_start=362
  _globals['_EVENTMANAGERSERVICE']._serialized_end=636
# @@protoc_insertion_point(module_scope)