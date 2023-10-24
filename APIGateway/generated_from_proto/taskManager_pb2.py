# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: taskManager.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x11taskManager.proto\"\x1d\n\nGetByEvent\x12\x0f\n\x07\x65ventId\x18\x01 \x01(\x05\"\x1d\n\x0bGetByTaskId\x12\x0e\n\x06taskId\x18\x01 \x01(\x05\"o\n\x0bTaskDetails\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x0f\n\x07\x65ventId\x18\x02 \x01(\x05\x12\x0c\n\x04name\x18\x03 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x04 \x01(\t\x12\x10\n\x08\x64\x65\x61\x64line\x18\x05 \x01(\t\x12\x0e\n\x06status\x18\x06 \x01(\t\"$\n\x05Tasks\x12\x1b\n\x05items\x18\x01 \x03(\x0b\x32\x0c.TaskDetails\"+\n\rCreateNewTask\x12\x1a\n\x04task\x18\x01 \x01(\x0b\x32\x0c.TaskDetails\"(\n\nUpdateTask\x12\x1a\n\x04task\x18\x01 \x01(\x0b\x32\x0c.TaskDetails\"\x1f\n\x11\x44\x65leteTaskRequest\x12\n\n\x02id\x18\x01 \x01(\x05\"\'\n\x12\x44\x65leteTaskResponse\x12\x11\n\tisDeleted\x18\x01 \x01(\x08\x32\x88\x02\n\x12TaskManagerService\x12\'\n\x10GetTaskListAsync\x12\x0b.GetByEvent\x1a\x06.Tasks\x12.\n\x10GetTaskByIdAsync\x12\x0c.GetByTaskId\x1a\x0c.TaskDetails\x12/\n\x0f\x43reateTaskAsync\x12\x0e.CreateNewTask\x1a\x0c.TaskDetails\x12,\n\x0fUpdateTaskAsync\x12\x0b.UpdateTask\x1a\x0c.TaskDetails\x12:\n\x0f\x44\x65leteTaskAsync\x12\x12.DeleteTaskRequest\x1a\x13.DeleteTaskResponseB\x1f\xaa\x02\x1cTaskManagementService.Protosb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'taskManager_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\252\002\034TaskManagementService.Protos'
  _globals['_GETBYEVENT']._serialized_start=21
  _globals['_GETBYEVENT']._serialized_end=50
  _globals['_GETBYTASKID']._serialized_start=52
  _globals['_GETBYTASKID']._serialized_end=81
  _globals['_TASKDETAILS']._serialized_start=83
  _globals['_TASKDETAILS']._serialized_end=194
  _globals['_TASKS']._serialized_start=196
  _globals['_TASKS']._serialized_end=232
  _globals['_CREATENEWTASK']._serialized_start=234
  _globals['_CREATENEWTASK']._serialized_end=277
  _globals['_UPDATETASK']._serialized_start=279
  _globals['_UPDATETASK']._serialized_end=319
  _globals['_DELETETASKREQUEST']._serialized_start=321
  _globals['_DELETETASKREQUEST']._serialized_end=352
  _globals['_DELETETASKRESPONSE']._serialized_start=354
  _globals['_DELETETASKRESPONSE']._serialized_end=393
  _globals['_TASKMANAGERSERVICE']._serialized_start=396
  _globals['_TASKMANAGERSERVICE']._serialized_end=660
# @@protoc_insertion_point(module_scope)
