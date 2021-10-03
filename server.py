import grpc
import message_pb2
import message_pb2_grpc
import time


class Information(message_pb2_grpc.InformationServicer):
    def RequestID(self, request, context):
        print(request, context)
        return message_pb2.IDReply(message='ID: %s' % id)


def serve():
    server = grpc.server(10)
    message_pb2_grpc.add_InformationServicer_to_server(Information(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        server.stop(0)


if __name__ == '__main__':
    serve()