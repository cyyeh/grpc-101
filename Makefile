protoc:
	pipenv run python -m grpc.tools.protoc --proto_path=protos --python_out=${PROTO_NAME} --grpc_python_out=${PROTO_NAME} protos/${PROTO_NAME}.proto
