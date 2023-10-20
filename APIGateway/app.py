import grpc
from flask import Flask

import communication_pb2
import communication_pb2_grpc

app = Flask(__name__)


@app.route('/')
def run():
    with grpc.insecure_channel('localhost:5116') as channel:
        stub = communication_pb2_grpc.CommunicationStub(channel)

        hello_request = communication_pb2.MessageRequest(message="Bonjour")
        hello_reply = stub.SendMessage(hello_request)
        print("SayHello Response Received:")
        print(hello_reply)
        return 'Hello'

if __name__ == '__main__':
    app.run()
