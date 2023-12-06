import threading
from concurrent import futures

import grpc
from flask import Flask, request, make_response, json, Response
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from google.protobuf.json_format import MessageToJson

from generated_from_proto import communication_pb2_grpc, communication_pb2
from handlers.event_handler import create_event_grpc, get_all_events_grpc, get_event_by_id_grpc, update_event_grpc, \
    delete_event_grpc
from handlers.task_handler import create_task_grpc, update_task_grpc, get_task_by_id_grpc, delete_task_grpc, \
    get_tasks_by_event_grpc
app = Flask(__name__)
limiter = Limiter(
    get_remote_address,
    app=app,
    default_limits=["3 per second"],
)
cache = {}
listOfEventManagerUrl = []
eventManagerUrl = ''


@app.before_request
def hook():
    if request.method == 'GET' and "get_all_events" in cache.keys():
        if request.endpoint == "get_all_events":
            print("Data from cache")
            test = cache[request.endpoint]
            return MessageToJson(cache[request.endpoint])
    if request.method == 'GET' and "get_event_by_id" in cache.keys():
        event_id = request.view_args.get('event_id')
        if "get_event_by_id" in cache and isinstance(cache["get_event_by_id"], list):
            for element in cache["get_event_by_id"]:
                if event_id == element.id:
                    print("Data from cache")
                    return MessageToJson(element)
    if request.method in ['POST', 'DELETE', 'PUT'] and "get_all_events" in cache.keys():
        del cache["get_all_events"]
    if request.method in ['DELETE', 'PUT'] and "get_event_by_id" in cache.keys():
        del cache["get_event_by_id"]

    if request.method == 'GET' and "get_tasks_by_event" in cache.keys():
        if request.endpoint == "get_tasks_by_event":
            print("Data from cache")
            return MessageToJson(cache[request.endpoint])
    if request.method == 'GET' and "get_task_by_id" in cache.keys():
        task_id = request.view_args.get('task_id')
        if "get_task_by_id" in cache and isinstance(cache["get_task_by_id"], list):
            for element in cache["get_task_by_id"]:
                if task_id == element.id:
                    print("Data from cache")
                    return MessageToJson(element)
    if request.method in ['POST', 'DELETE', 'PUT'] and "get_tasks_by_event" in cache.keys():
        del cache["get_tasks_by_event"]
    if request.method in ['DELETE', 'PUT'] and "get_task_by_id" in cache.keys():
        del cache["get_task_by_id"]


@app.route('/event', methods=['POST'])
def create_event():
    data = request.get_json()
    response = create_event_grpc(data)
    if isinstance(response, Response):
        return response
    else:
        return MessageToJson(response)


@app.route('/event', methods=['Get'])
def get_all_events():
    print("test")
    response = get_all_events_grpc()
    if isinstance(response, Response):
        return response
    else:
        cache[request.endpoint] = response
        print("Data from db")
        return MessageToJson(response)


@app.route('/event/<int:event_id>', methods=['GET'])
def get_event_by_id(event_id):
    response = get_event_by_id_grpc(event_id)
    if isinstance(response, Response):
        return response
    else:
        if request.endpoint in cache.keys():
            cache[request.endpoint].append(response)
        else:
            cache[request.endpoint] = [response]
        print("Data from db")
        return MessageToJson(response)


@app.route('/event/<int:event_id>', methods=['PUT'])
def update_event(event_id):
    data = request.get_json()
    response = update_event_grpc(event_id, data)
    if isinstance(response, Response):
        return response
    else:
        return MessageToJson(response)


@app.route('/event/<int:event_id>', methods=['DELETE'])
def delete_event(event_id):
    response = delete_event_grpc(event_id)
    if isinstance(response, Response):
        return response
    else:
        return MessageToJson(response)


@app.route('/task', methods=['POST'])
def create_task():
    data = request.get_json()
    list_event_id = []
    all_events = get_all_events_grpc()
    for event in all_events.items:
        event_id = event.id
        list_event_id.append(event_id)
    if data.get("eventId") in list_event_id:
        response = create_task_grpc(data)
        if isinstance(response, Response):
            return response
        else:
            return MessageToJson(response)
    else:
        return make_response("The event ID does not exists", 404)


@app.route('/task/eventId/<int:event_id>', methods=['Get'])
def get_tasks_by_event(event_id):
    response = get_tasks_by_event_grpc(event_id)
    if isinstance(response, Response):
        return response
    else:
        cache[request.endpoint] = response
        print("Data from db")
        return MessageToJson(response)


@app.route('/task/<int:task_id>', methods=['GET'])
def get_task_by_id(task_id):
    print("test")
    response = get_task_by_id_grpc(task_id)

    if isinstance(response, Response):
        return response
    else:
        if request.endpoint in cache.keys():
            cache[request.endpoint].append(response)
        else:
            cache[request.endpoint] = [response]
        print("Data from db")
        return MessageToJson(response)


@app.route('/task/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    data = request.get_json()
    response = update_task_grpc(task_id, data)
    if isinstance(response, Response):
        return response
    else:
        return MessageToJson(response)


@app.route('/task/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    response = delete_task_grpc(task_id)
    if isinstance(response, Response):
        return response
    else:
        return MessageToJson(response)


class CommunicationServicer(communication_pb2_grpc.CommunicationServicer):

    def SendMessage(self, request, context):
        print(f"Service url:{request.message}.")
        if request.sender == 'Event manager':
            listOfEventManagerUrl.append(request.message)
        print(listOfEventManagerUrl)
        hello_reply = communication_pb2.MessageResponse()
        hello_reply.message = f"Service {request.message} was successfully registered in gateway."
        return hello_reply


def grpc_server():
    stop_event = threading.Event()
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    communication_pb2_grpc.add_CommunicationServicer_to_server(CommunicationServicer(), server)
    server.add_insecure_port("[::]:5003")
    try:
        server.start()
        print("grpc server started at port : 5000")
        stop_event.wait()

    except Exception as e:
        print(f"ERROR on running grpc server: {e}")
        server.stop(0)


grpc_server_thread = threading.Thread(target=grpc_server)
grpc_server_thread.start()