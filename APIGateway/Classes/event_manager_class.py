import grpc
from flask import make_response, Response
from pybreaker import CircuitBreaker

from generated_from_proto import eventManager_pb2_grpc, eventManager_pb2
from load_balancer import get_url


class EventManagerClass:
    def __init__(self):
        self.breaker = CircuitBreaker(fail_max=3, reset_timeout=10, exclude=[
            lambda e: isinstance(e, grpc.RpcError) and e.code() == grpc.StatusCode.NOT_FOUND
        ])

    @property
    def get_all_events(self):
        @self.breaker
        def get_all_events_internal(url):
            print(f"{url} {self.breaker.state}")
            channel = grpc.insecure_channel(url)
            stub = eventManager_pb2_grpc.EventManagerServiceStub(channel)
            request = eventManager_pb2.Empty()
            try:
                response = stub.GetEventListAsync(request)
            except Exception as e:
                raise Exception(e)

            if response is None:
                return make_response('No events', 200)
            else:
                return response

        return get_all_events_internal

    @property
    def get_event_by_id(self):
        @self.breaker
        def get_event_by_id_internal(url, event_id):
            channel = grpc.insecure_channel(url)
            stub = eventManager_pb2_grpc.EventManagerServiceStub(channel)
            request = eventManager_pb2.GetByEventId(id=event_id)
            try:
                response = stub.GetEventByIdAsync(request)
                if response is None:
                    return make_response('Event not found', 404)
                else:
                    return response

            except grpc.RpcError as err:
                if err.code() == grpc.StatusCode.NOT_FOUND:
                    return make_response('Event not found', 404)
                else:
                    raise Exception(err)
            except Exception as e:
                raise Exception(e)
            #
            #

        return get_event_by_id_internal

    @property
    def create_event(self):
        @self.breaker
        def create_event_internal(url, data):
            channel = grpc.insecure_channel(url)
            stub = eventManager_pb2_grpc.EventManagerServiceStub(channel)
            request = request = eventManager_pb2.EventDetails(name=data.get("name"),
                                                              date=data.get("date"),
                                                              location=data.get("location"),
                                                              dressCode=data.get("dressCode"))
            new_event = eventManager_pb2.CreateNewEvent()
            new_event.event.CopyFrom(request)
            try:
                response = stub.CreateEventAsync(new_event)
                return response
            except grpc.RpcError as err:
                print(f"grpc error: {err.code()}")
                raise Exception(err)
            except Exception as e:
                raise Exception(e)
        return create_event_internal

    @property
    def update_event(self):
        @self.breaker
        def update_event_internal(url, event_id, data):
            channel = grpc.insecure_channel(url)
            stub = eventManager_pb2_grpc.EventManagerServiceStub(channel)
            request = eventManager_pb2.EventDetails(id=event_id,
                                                    name=data.get("name"),
                                                    date=data.get("date"),
                                                    location=data.get("location"),
                                                    dressCode=data.get("dressCode")
                                                    )
            updated_event = eventManager_pb2.UpdateEvent()
            updated_event.event.CopyFrom(request)
            try:
                response = stub.UpdateEventAsync(updated_event)
                return response
            except grpc.RpcError as err:
                print(f"grpc error: {err.code()}")
                if err.code() == grpc.StatusCode.NOT_FOUND:
                    return make_response('Event not found', 404)
                else:
                    raise Exception(err)
            except Exception as e:
                raise Exception(e)

        return update_event_internal

    @property
    def delete_event(self):
        @self.breaker
        def delete_event_internal(url, event_id):
            channel = grpc.insecure_channel(url)
            stub = eventManager_pb2_grpc.EventManagerServiceStub(channel)
            request = eventManager_pb2.DeleteEventRequest(id=event_id)

            try:
                response = stub.DeleteEventAsync(request)
                return response

            except grpc.RpcError as err:
                print(f"grpc error: {err.code()}")
                if err.code() == grpc.StatusCode.NOT_FOUND:
                    return make_response('Event not found', 404)
                else:
                    raise Exception(err)
            except Exception as e:
                raise Exception(e)
        return delete_event_internal
