# gRPC 101

This project is a hello-world project for demonstrating how to use gRPC to communicate between clients and servers.

## Quick Start

1. `pipenv install`: Preparing the python3.7 development environment with required dependencies
2. `PROTO_NAME=greeter make protoc`: It will generate `greeter_pb2_grpc.py` and `greeter_pb2.py` inside the greeter folder
3. `pipenv run python greeter/greeter_server.py`: Initiate the grpc server
4. `pipenv run python greeter/greeter_client.py`: Send a request from the client to the grpc server

## See a More Detailed Example Here

1. `PROTO_NAME=route_guide make protoc`: It will generate `route_guide_pb2_grpc.py` and `route_guide_pb2.py` inside the route_guide folder
2. `pipenv run python route_guide/route_guide_server.py`: Initiate the grpc server
3. `pipenv run python route_guide/route_guide_client.py`: Send requests from the client to the grpc server

## General Workflow for Using gRPC

See [here](https://grpc.io/docs/languages/python/basics/) for more detailed information

1. Defining the service: define the gRPC service and the method request and response types using protocol buffers
2. Generating client and server code: generate the gRPC client and server interfaces from your .proto service definition using `protoc`, the protocol buffer compiler
3. Creating the server/Creating the client

## References

- [gRPC official website](https://grpc.io/)
  - [Introduction](https://grpc.io/docs/what-is-grpc/introduction/)
  - [Core concepts](https://grpc.io/docs/what-is-grpc/core-concepts/)
  - [Motivation and Design Principles](https://grpc.io/blog/principles/)
- [gRPC for Python](https://grpc.io/docs/languages/python/)
  - [gRPC Examples for Python](https://github.com/grpc/grpc/tree/master/examples/python)
- [Protocol Buffer Language Guide](https://developers.google.com/protocol-buffers/docs/overview)