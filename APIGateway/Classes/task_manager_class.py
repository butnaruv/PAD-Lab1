import grpc
from flask import make_response
from pybreaker import CircuitBreaker

from generated_from_proto import taskManager_pb2_grpc, taskManager_pb2


class TaskManagerClass:
    def __init__(self):
        self.breaker = CircuitBreaker(fail_max=3, reset_timeout=10, exclude=[
            lambda e: isinstance(e, grpc.RpcError) and e.code() == grpc.StatusCode.NOT_FOUND
        ])

    @property
    def get_tasks_by_event(self):
        @self.breaker
        def get_tasks_by_events_internal(url, event_id):
            channel = grpc.insecure_channel(url)
            stub = taskManager_pb2_grpc.TaskManagerServiceStub(channel)
            request = taskManager_pb2.GetByEvent(eventId=event_id)
            try:
                response = stub.GetTaskListAsync(request)
            except Exception as e:
                raise Exception(e)

            if response is None:
                return make_response('No events', 200)
            else:
                return response

        return get_tasks_by_events_internal

    @property
    def create_task(self):
        @self.breaker
        def create_task_internal(url, data):
            channel = grpc.insecure_channel(url)
            stub = taskManager_pb2_grpc.TaskManagerServiceStub(channel)

            request = taskManager_pb2.TaskDetails(name=data.get("name"),
                                                  eventId=data.get("eventId"),
                                                  description=data.get("description"),
                                                  deadline=data.get("deadline"),
                                                  status=data.get("status")
                                                  )
            new_task = taskManager_pb2.CreateNewTask()
            new_task.task.CopyFrom(request)
            try:
                response = stub.CreateTaskAsync(new_task)
                return response
            except grpc.RpcError as err:
                print(f"grpc error: {err.code()}")
                raise Exception(err)
            except Exception as e:
                raise Exception(e)

        return create_task_internal

    @property
    def get_task_by_id(self):
        @self.breaker
        def get_task_by_id_internal(url, task_id):
            channel = grpc.insecure_channel(url)
            stub = taskManager_pb2_grpc.TaskManagerServiceStub(channel)
            request = taskManager_pb2.GetByTaskId(taskId=task_id)
            try:
                response = stub.GetTaskByIdAsync(request)
                return response
            except grpc.RpcError as err:
                if err.code() == grpc.StatusCode.NOT_FOUND:
                    return make_response('Task not found', 404)
                print(f"grpc error: {err.code()}")
                raise Exception(err)
            except Exception as e:
                raise Exception(e)
        return get_task_by_id_internal

    @property
    def update_task(self):
        @self.breaker
        def update_task_internal(url, task_id, data):
            channel = grpc.insecure_channel(url)
            stub = taskManager_pb2_grpc.TaskManagerServiceStub(channel)
            request = taskManager_pb2.TaskDetails(id=task_id,
                                                  name=data.get("name"),
                                                  description=data.get("description"),
                                                  deadline=data.get("deadline"),
                                                  status=data.get("status")
                                                  )
            updated_task = taskManager_pb2.UpdateTask()
            updated_task.task.CopyFrom(request)
            try:
                response = stub.UpdateTaskAsync(updated_task)
                return response
            except grpc.RpcError as err:
                if err.code() == grpc.StatusCode.NOT_FOUND:
                    return make_response('Task not found', 404)
                print(f"grpc error: {err.code()}")
                raise Exception(err)
            except Exception as e:
                raise Exception(e)

        return update_task_internal

    @property
    def delete_task(self):
        @self.breaker
        def delete_task_internal(url, task_id):
            channel = grpc.insecure_channel(url)
            stub = taskManager_pb2_grpc.TaskManagerServiceStub(channel)
            request = taskManager_pb2.DeleteTaskRequest(id=task_id)
            try:
                response = stub.DeleteTaskAsync(request)
                return response
            except grpc.RpcError as err:
                if err.code() == grpc.StatusCode.NOT_FOUND:
                    return make_response('Task not found', 404)
                print(f"grpc error: {err.code()}")
                raise Exception(err)
            except Exception as e:
                raise Exception(e)

        return delete_task_internal