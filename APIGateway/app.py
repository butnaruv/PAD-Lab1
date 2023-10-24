from flask import Flask, request, make_response, json, Response
from google.protobuf.json_format import MessageToJson

from handlers.event_handler import create_event_grpc, get_all_events_grpc, get_event_by_id_grpc, update_event_grpc, \
    delete_event_grpc
from handlers.task_handler import create_task_grpc, update_task_grpc, get_task_by_id_grpc, delete_task_grpc, \
    get_tasks_by_event_grpc

app = Flask(__name__)

list = []


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
    response = get_all_events_grpc()
    if isinstance(response, Response):
        return response
    else:
        return MessageToJson(response)


@app.route('/event/<int:event_id>', methods=['GET'])
def get_event_by_id(event_id):
    response = get_event_by_id_grpc(event_id)
    if isinstance(response, Response):
        return response
    else:
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


# @app.route('/event/cahe', methods=['GET'])
# def print_cache():
#     print(list)
#     return json.dumps(list)


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
        return MessageToJson(response)


@app.route('/task/<int:task_id>', methods=['GET'])
def get_task_by_id(task_id):
    print("test")
    response = get_task_by_id_grpc(task_id)

    if isinstance(response, Response):
        return response
    else:
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


if __name__ == '__main__':
    app.run()
