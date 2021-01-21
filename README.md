# gRPC 101

This project is a hello-world project for demonstrating how to use gRPC to communicate between clients and servers.

## Quick Start

1. `pipenv install`: Preparing the python3.7 development environment with required dependencies
2. `PROTO_NAME=helloworld make protoc`: It will generate `helloworld_pb2_grpc.py` and `helloworld_pb2.py` inside the grpc folder
3. `make run`: Initiate the grpc server
4. `make request`: Send a request from client to the grpc server

## References

- [gRPC official website](https://grpc.io/)
  - [Introduction](https://grpc.io/docs/what-is-grpc/introduction/)
  - [Core concepts](https://grpc.io/docs/what-is-grpc/core-concepts/)
  - [Motivation and Design Principles](https://grpc.io/blog/principles/)
- [gRPC for Python](https://grpc.io/docs/languages/python/)
  - [gRPC Examples for Python](https://github.com/grpc/grpc/tree/master/examples/python)