# reference: https://github.com/grpc/grpc/blob/master/examples/python/helloworld/greeter_client.py
import logging

import grpc

import helloworld_pb2
import helloworld_pb2_grpc


def run():
    with grpc.insecure_channel('localhost:8000') as channel:
        stub = helloworld_pb2_grpc.GreeterStub(channel)
        response = stub.SayHello(helloworld_pb2.HelloRequest(name='you'))
    print('Greeter client received: ' + response.message)


if __name__ == '__main__':
    logging.basicConfig()
    run()
