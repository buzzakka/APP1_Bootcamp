Для генерации файлов используется следующая команда:

`python -m grpc_tools.protoc --proto_path=. ./galaxy.proto --python_out=. --grpc_python_out=. --pyi_out=.`