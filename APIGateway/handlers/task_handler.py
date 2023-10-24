import grpc
from flask import make_response

from generated_from_proto import taskManager_pb2_grpc, taskManager_pb2


def create_task_grpc(data):
    with grpc.insecure_channel('localhost:5192') as channel:
        stub = taskManager_pb2_grpc.TaskManagerServiceStub(channel)

        request = taskManager_pb2.TaskDetails(name=data.get("name"),
                                              eventId=data.get("eventId"),
                                              description=data.get("description"),
                                              deadline=data.get("deadline"),
                                              status=data.get("status")
                                              )

        test = taskManager_pb2.CreateNewTask()
        test.task.CopyFrom(request)
        try:
            response = stub.CreateTaskAsync(test)
        except Exception as e:
            print(e)
            exception_str = str(e)
            if "Timeout error" in exception_str:
                return make_response('Task timeout', 408)
            else:
                return make_response('Creation failed', 500)
        return response


def get_task_by_id_grpc(task_id):
    with grpc.insecure_channel('localhost:5192') as channel:
        stub = taskManager_pb2_grpc.TaskManagerServiceStub(channel)
        request = taskManager_pb2.GetByTaskId(taskId=task_id)
        try:
            response = stub.GetTaskByIdAsync(request)
        except Exception as e:
            print(e)
            exception_str = str(e)
            if "Timeout error" in exception_str:
                return make_response('Task timeout', 408)
            elif "No message returned from method" in exception_str:
                return make_response('Task not found', 404)
            else:
                return make_response('Request failed', 500)
        if response is None:
            return make_response('Task not found', 404)
        else:
            return response


def get_tasks_by_event_grpc(event_id):
    with grpc.insecure_channel('localhost:5192') as channel:
        stub = taskManager_pb2_grpc.TaskManagerServiceStub(channel)
        request = taskManager_pb2.GetByEvent(eventId=event_id)
        response = None
        try:
            response = stub.GetTaskListAsync(request)
        except Exception as e:
            print(e)
            exception_str = str(e)
            if "Timeout error" in exception_str:
                return make_response('Task timeout', 408)
        nr_of_tasks = 0
        for task in response.items:
            nr_of_tasks = nr_of_tasks + 1
        if nr_of_tasks != 0:
            return response
        else:
            return make_response('No tasks assigned to this event', 404)


def update_task_grpc(task_id, data):
    with grpc.insecure_channel('localhost:5192') as channel:
        stub = taskManager_pb2_grpc.TaskManagerServiceStub(channel)

        # Create a request message with the event ID
        request = taskManager_pb2.TaskDetails(id=task_id,
                                              name=data.get("name"),
                                              description=data.get("description"),
                                              deadline=data.get("deadline"),
                                              status=data.get("status")
                                              )
        test = taskManager_pb2.UpdateTask()
        test.task.CopyFrom(request)

        try:
            response = stub.UpdateTaskAsync(test)
        except Exception as e:
            print(e)
            exception_str = str(e)
            if "Timeout error" in exception_str:
                return make_response('Task timeout', 408)
            else:
                return make_response('Update failed', 418)
        if response is not None:
            return response
        else:
            return make_response('Update failed', 418)

def delete_task_grpc(task_id):
    with grpc.insecure_channel('localhost:5192') as channel:
        stub = taskManager_pb2_grpc.TaskManagerServiceStub(channel)
        request = taskManager_pb2.DeleteTaskRequest(id=task_id)

        try:
            response = stub.DeleteTaskAsync(request)
        except Exception as e:
            print(e)
            exception_str = str(e)
            if "Timeout error" in exception_str:
                return make_response('Task timeout', 408)
            else:
                return make_response('Delete failed', 418)
        if response is not None:
            return response
        else:
            return make_response('Event not found', 404)
