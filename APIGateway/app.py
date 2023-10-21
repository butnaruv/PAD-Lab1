from flask import Flask, request, make_response
from google.protobuf.json_format import MessageToJson

from handlers.event_handler import create_event_grpc, get_all_events_grpc, get_event_by_id_grpc, update_event_grpc, \
    delete_event_grpc

app = Flask(__name__)


@app.route('/event', methods=['POST'])
def create_event():
    data = request.get_json()
    create_event_grpc(data)
    return make_response('Event created successfully', 201)


@app.route('/event', methods=['Get'])
def get_all_events():
    response = get_all_events_grpc()
    return MessageToJson(response)


@app.route('/event/<int:event_id>', methods=['GET'])
def get_event_by_id(event_id):
    response = get_event_by_id_grpc(event_id)

    if response is not None:
        event_json = MessageToJson(response)
        return event_json
    else:
        return make_response('Event not found', 404)


@app.route('/event/<int:event_id>', methods=['PUT'])
def update_event(event_id):
    data = request.get_json()
    response = update_event_grpc(event_id, data)
    if response is not None:
        event_json = MessageToJson(response)
        return event_json
    else:
        return make_response('Event not found', 404)


@app.route('/event/<int:event_id>', methods=['DELETE'])
def delete_event(event_id):
    response = delete_event_grpc(event_id)
    if response is not None:
        return make_response('Event was deleted', 201)
    else:
        return make_response('Event not found', 404)


if __name__ == '__main__':
    app.run()
