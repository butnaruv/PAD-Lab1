import grpc
from flask import make_response

from generated_from_proto import eventManager_pb2_grpc, eventManager_pb2, communication_pb2_grpc, communication_pb2
from load_balancer import get_url


def create_event_grpc(data):
    with grpc.insecure_channel(get_url()) as channel:
        stub = eventManager_pb2_grpc.EventManagerServiceStub(channel)

        request = eventManager_pb2.EventDetails(name=data.get("name"),
                                                date=data.get("date"),
                                                location=data.get("location"),
                                                dressCode=data.get("dressCode"))

        test = eventManager_pb2.CreateNewEvent()
        test.event.CopyFrom(request)
        try:
            response = stub.CreateEventAsync(test)
        except Exception as e:
            print(e)
            exception_str = str(e)
            if "Timeout error" in exception_str:
                return make_response('Task timeout', 408)
            else:
                return make_response('Creation failed', 500)
    return response


def get_all_events_grpc():
    with grpc.insecure_channel(get_url()) as channel:
        stub = eventManager_pb2_grpc.EventManagerServiceStub(channel)
        request = eventManager_pb2.Empty()
        try:
            response = stub.GetEventListAsync(request)
        except Exception as e:
            print(e)
            exception_str = str(e)
            if "Timeout error" in exception_str:
                return make_response('Task timeout', 408)
            else:
                return make_response('Request failed', 500)
    if response is None:
        return make_response('No events', 200)
    else:
        return response


def get_event_by_id_grpc(event_id):
    with grpc.insecure_channel(get_url()) as channel:
        stub = eventManager_pb2_grpc.EventManagerServiceStub(channel)
        request = eventManager_pb2.GetByEventId(id=event_id)
        response = None
        try:
            response = stub.GetEventByIdAsync(request)
        except Exception as e:
            print(e)
            exception_str = str(e)
            if "Timeout error" in exception_str:
                return make_response('Task timeout', 408)
        if response is not None:
            return response
        else:
            return make_response('Event not found', 404)


def update_event_grpc(event_id, data):
    with grpc.insecure_channel(get_url()) as channel:
        stub = eventManager_pb2_grpc.EventManagerServiceStub(channel)

        # Create a request message with the event ID
        request = eventManager_pb2.EventDetails(id=event_id,
                                                name=data.get("name"),
                                                date=data.get("date"),
                                                location=data.get("location"),
                                                dressCode=data.get("dressCode")
                                                )
        test = eventManager_pb2.UpdateEvent()
        test.event.CopyFrom(request)
        try:
            response = stub.UpdateEventAsync(test)
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


def delete_event_grpc(event_id):
    with grpc.insecure_channel(get_url()) as channel:
        stub = eventManager_pb2_grpc.EventManagerServiceStub(channel)
        request = eventManager_pb2.DeleteEventRequest(id=event_id)

        try:
            response = stub.DeleteEventAsync(request)
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
