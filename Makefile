protoc:
	pipenv run python -m grpc.tools.protoc --proto_path=protos --python_out=grpc --grpc_python_out=grpc protos/${PROTO_NAME}.proto

run:
	pipenv run python grpc/greeter_server.py

request:
	pipenv run python grpc/greeter_client.py