import grpc

from generated_from_proto import eventManager_pb2_grpc, eventManager_pb2, communication_pb2_grpc, communication_pb2


def create_event_grpc(data):
    with grpc.insecure_channel('localhost:5116') as channel:
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
        print("Event was added with the next details:")
        print(response)
        return response


def get_all_events_grpc():
    with grpc.insecure_channel('localhost:5116') as channel:
        stub = eventManager_pb2_grpc.EventManagerServiceStub(channel)
        request = eventManager_pb2.Empty()
        response = stub.GetEventListAsync(request)
        print(response)
        return response


def get_event_by_id_grpc(event_id):
    with grpc.insecure_channel('localhost:5116') as channel:
        stub = eventManager_pb2_grpc.EventManagerServiceStub(channel)
        request = eventManager_pb2.GetByEventId(id=event_id)

        try:
            response = stub.GetEventByIdAsync(request)
            print(response)
            return response
        except Exception as e:
            print(e)
            return None


def update_event_grpc(event_id, data):
    with grpc.insecure_channel('localhost:5116') as channel:
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
            print(response)
            return response
        except Exception as e:
            print(e)
            return None


def delete_event_grpc(event_id):
    with grpc.insecure_channel('localhost:5116') as channel:
        stub = eventManager_pb2_grpc.EventManagerServiceStub(channel)
        request = eventManager_pb2.DeleteEventRequest(id=event_id)

        try:
            response = stub.DeleteEventAsync(request)
            print(response)
            return response
        except Exception as e:
            print(e)
            return None
