import threading
import time
from concurrent import futures

import circuitbreaker
import grpc
import pybreaker
import requests
from circuitbreaker import circuit
from flask import Flask, request, make_response, json, Response
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from google.protobuf.json_format import MessageToJson
from generated_from_proto import communication_pb2_grpc, communication_pb2
from handlers.event_handler import create_event_grpc, get_event_by_id_grpc, update_event_grpc, \
    delete_event_grpc, get_all_events_grpc
from handlers.task_handler import create_task_grpc, update_task_grpc, get_task_by_id_grpc, delete_task_grpc, \
    get_tasks_by_event_grpc
from load_balancer import load_balance_requests, get_url, reset_index
from Classes.event_manager_class import EventManagerClass

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


def remove_route(url):
    print(f"Initial list of services: {listOfEventManagerUrl}")
    element = "http://" + url
    if element in listOfEventManagerUrl:
        listOfEventManagerUrl.remove(element)
        print(f"Url is removed. Updated list: {listOfEventManagerUrl}")

@app.route('/event', methods=['POST'])
def create_event():
    data = request.get_json()
    url = get_url()
    if isinstance(url, Response):
        return url
    event_manager = EventManagerClass()
    breaker = event_manager.breaker
    try:
        create_event_function = event_manager.create_event
        response = create_event_function(url, data)
    except Exception  as e:
        while breaker.state.name == "closed":
            try:
                response = create_event_function(url, data)
                return response
            except Exception as e:
                print()

        if breaker.state.name == "open":
            remove_route(url)
            print(f"Rerouting activat")
            reset_index()
            return create_event()

    if isinstance(response, Response):
        return response
    else:
        return MessageToJson(response)


@app.route('/event', methods=['Get'])
def get_all_events():
    url = get_url()
    if isinstance(url, Response):
        return url
    event_manager = EventManagerClass()
    breaker = event_manager.breaker
    print(breaker.fail_max)
    try:
        get_all_events_function = event_manager.get_all_events
        response = get_all_events_function(url)
    except Exception  as e:
        while breaker.state.name == "closed":
            try:
                response = get_all_events_function(url)
                return MessageToJson(response)
            except Exception as e:
                print()
        if breaker.state.name == "open":
            remove_route(url)
            print(f"Rerouting activat")
            reset_index()
            return get_all_events()

    if isinstance(response, Response):
        return response
    else:
        cache[request.endpoint] = response
        print("Data from db")
        return MessageToJson(response)


@app.route('/event/<int:event_id>', methods=['GET'])
def get_event_by_id(event_id):
    url = get_url()
    if isinstance(url, Response):
        return url

    event_manager = EventManagerClass()
    breaker = event_manager.breaker
    try:
        get_event_by_id_function = event_manager.get_event_by_id
        response = get_event_by_id_function(url, event_id)
    except Exception as e:
        while breaker.state.name == "closed":
            try:
                response = get_event_by_id_function(url, event_id)
                return response
            except Exception as e:
                print()
        if breaker.state.name == "open":
            remove_route(url)
            print(f"Rerouting activat")
            reset_index()
            return get_event_by_id(event_id)

    if isinstance(response, Response):
        return make_response("No more services available")
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
    url = get_url()
    if isinstance(url, Response):
        return url
    event_manager = EventManagerClass()
    breaker = event_manager.breaker
    try:
        update_event_function = event_manager.update_event
        response = update_event_function(url, event_id, data)
    except Exception as e:
        while breaker.state.name == "closed":
            try:
                response = update_event_function(url, event_id, data)
                return response
            except Exception as e:
                print()
        if breaker.state.name == "open":
            remove_route(url)
            print(f"Rerouting activat")
            reset_index()
            return update_event(event_id)

    if isinstance(response, Response):
        return response
    else:
        return MessageToJson(response)



@app.route('/event/<int:event_id>', methods=['DELETE'])
def delete_event(event_id):
    url = get_url()
    if isinstance(url, Response):
        return url
    event_manager = EventManagerClass()
    breaker = event_manager.breaker
    try:
        delete_event_function = event_manager.delete_event
        response = delete_event_function(url, event_id)
    except Exception as e:
        while breaker.state.name == "closed":
            try:
                response = delete_event_function(url, event_id)
                return response
            except Exception as e:
                print()
        if breaker.state.name == "open":
            remove_route(url)
            print(f"Rerouting activat")
            reset_index()
            return delete_event(event_id)

    if isinstance(response, Response):
        return response
    else:
        return MessageToJson(response)


@app.route('/task', methods=['POST'])
def create_task():
    data = request.get_json()
    list_event_id = []
    url = get_url()
    if isinstance(url, Response):
        return url
    all_events = get_all_events_grpc(url)
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
    url = get_url()
    if isinstance(url, Response):
        return url
    response = get_tasks_by_event_grpc(event_id, url)
    if isinstance(response, Response):
        return response
    else:
        cache[request.endpoint] = response
        print("Data from db")
        return MessageToJson(response)


@app.route('/task/<int:task_id>', methods=['GET'])
def get_task_by_id(task_id):
    url = get_url()
    if isinstance(url, Response):
        return url
    response = get_task_by_id_grpc(task_id, url)

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
    url = get_url()
    if isinstance(url, Response):
        return url
    response = update_task_grpc(task_id, data, url)
    if isinstance(response, Response):
        return response
    else:
        return MessageToJson(response)


@app.route('/task/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    url = get_url()
    if isinstance(url, Response):
        return url
    response = delete_task_grpc(task_id, url)
    if isinstance(response, Response):
        return response
    else:
        return MessageToJson(response)




class CommunicationServicer(communication_pb2_grpc.CommunicationServicer):

    def SendMessage(self, request, context):
        print(f"Service url:{request.message}.")
        if request.sender == 'Event manager' and request.message not in listOfEventManagerUrl:
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
