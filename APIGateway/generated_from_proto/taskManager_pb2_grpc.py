# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import generated_from_proto.taskManager_pb2 as taskManager__pb2


class TaskManagerServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetTaskListAsync = channel.unary_unary(
                '/TaskManagerService/GetTaskListAsync',
                request_serializer=taskManager__pb2.GetByEvent.SerializeToString,
                response_deserializer=taskManager__pb2.Tasks.FromString,
                )
        self.GetTaskByIdAsync = channel.unary_unary(
                '/TaskManagerService/GetTaskByIdAsync',
                request_serializer=taskManager__pb2.GetByTaskId.SerializeToString,
                response_deserializer=taskManager__pb2.TaskDetails.FromString,
                )
        self.CreateTaskAsync = channel.unary_unary(
                '/TaskManagerService/CreateTaskAsync',
                request_serializer=taskManager__pb2.CreateNewTask.SerializeToString,
                response_deserializer=taskManager__pb2.TaskDetails.FromString,
                )
        self.UpdateTaskAsync = channel.unary_unary(
                '/TaskManagerService/UpdateTaskAsync',
                request_serializer=taskManager__pb2.UpdateTask.SerializeToString,
                response_deserializer=taskManager__pb2.TaskDetails.FromString,
                )
        self.DeleteTaskAsync = channel.unary_unary(
                '/TaskManagerService/DeleteTaskAsync',
                request_serializer=taskManager__pb2.DeleteTaskRequest.SerializeToString,
                response_deserializer=taskManager__pb2.DeleteTaskResponse.FromString,
                )


class TaskManagerServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def GetTaskListAsync(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetTaskByIdAsync(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CreateTaskAsync(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateTaskAsync(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteTaskAsync(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_TaskManagerServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetTaskListAsync': grpc.unary_unary_rpc_method_handler(
                    servicer.GetTaskListAsync,
                    request_deserializer=taskManager__pb2.GetByEvent.FromString,
                    response_serializer=taskManager__pb2.Tasks.SerializeToString,
            ),
            'GetTaskByIdAsync': grpc.unary_unary_rpc_method_handler(
                    servicer.GetTaskByIdAsync,
                    request_deserializer=taskManager__pb2.GetByTaskId.FromString,
                    response_serializer=taskManager__pb2.TaskDetails.SerializeToString,
            ),
            'CreateTaskAsync': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateTaskAsync,
                    request_deserializer=taskManager__pb2.CreateNewTask.FromString,
                    response_serializer=taskManager__pb2.TaskDetails.SerializeToString,
            ),
            'UpdateTaskAsync': grpc.unary_unary_rpc_method_handler(
                    servicer.UpdateTaskAsync,
                    request_deserializer=taskManager__pb2.UpdateTask.FromString,
                    response_serializer=taskManager__pb2.TaskDetails.SerializeToString,
            ),
            'DeleteTaskAsync': grpc.unary_unary_rpc_method_handler(
                    servicer.DeleteTaskAsync,
                    request_deserializer=taskManager__pb2.DeleteTaskRequest.FromString,
                    response_serializer=taskManager__pb2.DeleteTaskResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'TaskManagerService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class TaskManagerService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def GetTaskListAsync(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/TaskManagerService/GetTaskListAsync',
            taskManager__pb2.GetByEvent.SerializeToString,
            taskManager__pb2.Tasks.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetTaskByIdAsync(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/TaskManagerService/GetTaskByIdAsync',
            taskManager__pb2.GetByTaskId.SerializeToString,
            taskManager__pb2.TaskDetails.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CreateTaskAsync(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/TaskManagerService/CreateTaskAsync',
            taskManager__pb2.CreateNewTask.SerializeToString,
            taskManager__pb2.TaskDetails.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def UpdateTaskAsync(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/TaskManagerService/UpdateTaskAsync',
            taskManager__pb2.UpdateTask.SerializeToString,
            taskManager__pb2.TaskDetails.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DeleteTaskAsync(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/TaskManagerService/DeleteTaskAsync',
            taskManager__pb2.DeleteTaskRequest.SerializeToString,
            taskManager__pb2.DeleteTaskResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
