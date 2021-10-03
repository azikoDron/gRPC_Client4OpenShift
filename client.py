import grpc
import message_pb2
import message_pb2_grpc

SERVER_ADDRESS = "localhost:23333"


def main():
    with grpc.secure_channel(
            SERVER_ADDRESS,
            credentials=grpc.alts_channel_credentials()) as channel:
        stub = message_pb2_grpc.InformationStub(channel)

        message_pb2.IDRequest(requestID='222', body='a')
        response = stub.RequestID
        print(response)
        # simple_method(stub)
        # client_streaming_method(stub)
        # server_streaming_method(stub)
        # bidirectional_streaming_method(stub)


if __name__ == '__main__':
    main()