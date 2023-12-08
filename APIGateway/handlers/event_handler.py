import grpc
from flask import make_response, Response
from pybreaker import CircuitBreaker

from circuit_breaker import circuit_breaker
from generated_from_proto import eventManager_pb2_grpc, eventManager_pb2, communication_pb2_grpc, communication_pb2
from load_balancer import load_balance_requests, get_url

breaker = CircuitBreaker(fail_max=3, reset_timeout=10)

def create_event_grpc(data, url):
    with grpc.insecure_channel(url) as channel:
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

@breaker
def get_all_events_grpc(url):
    print(f"url to connect to: {url}")
    with grpc.insecure_channel(url) as channel:
        stub = eventManager_pb2_grpc.EventManagerServiceStub(channel)
        request = eventManager_pb2.Empty()
        try:
            response = stub.GetEventListAsync(request)
        except Exception as e:
            print("Exception when calling GetEventListAsync: ")
            raise Exception(e)
            # exception_str = str(e)

            # if "Timeout error" in exception_str:
            #     print("Task timeout")
            #     return make_response('Task timeout', 408)
            # else:
            #     print("Request failed")
            #     stop = circuit_breaker()
            #     if stop:
            #         url = get_url()
            #         if isinstance(url, Response):
            #             return url
            #         else:
            #             new_url = get_url()
            #             if new_url == url:
            #                 return make_response('The services are not available')
            #             else:
            #                 return get_all_events_grpc(get_url())
            #     else:
            #         return get_all_events_grpc(url)
    if response is None:
        return make_response('No events', 200)
    else:
        return response


def get_event_by_id_grpc(event_id, url):
    with grpc.insecure_channel(url) as channel:
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


def update_event_grpc(event_id, data, url):
    with grpc.insecure_channel(url) as channel:
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


def delete_event_grpc(event_id, url):
    with grpc.insecure_channel(url) as channel:
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
