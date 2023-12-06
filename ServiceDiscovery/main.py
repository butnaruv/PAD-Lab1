# This is a sample Python script.
import grpc
from concurrent import futures
import communication_pb2
import communication_pb2_grpc


# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


class CommunicationServicer(communication_pb2_grpc.CommunicationServicer):

    def SendMessage(self, request, context):
        print(request.sender)
        print(request.message)
        with grpc.insecure_channel('localhost:5003') as channel:
            stub = communication_pb2_grpc.CommunicationStub(channel)
            requestObject = communication_pb2.MessageRequest(sender=request.sender,
                                                             message=request.message)
            response = stub.SendMessage(requestObject)

        hello_reply = communication_pb2.MessageResponse()
        hello_reply.message = response.message
        print()
        return hello_reply


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    communication_pb2_grpc.add_CommunicationServicer_to_server(CommunicationServicer(), server)
    server.add_insecure_port("[::]:50051")
    server.start()
    server.wait_for_termination()

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    serve()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
