# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import proto.galaxy_pb2 as galaxy__pb2


class GalaxyStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.get_ships = channel.unary_stream(
                '/ex01.Galaxy/get_ships',
                request_serializer=galaxy__pb2.GalacticPossition.SerializeToString,
                response_deserializer=galaxy__pb2.Ship.FromString,
                )


class GalaxyServicer(object):
    """Missing associated documentation comment in .proto file."""

    def get_ships(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_GalaxyServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'get_ships': grpc.unary_stream_rpc_method_handler(
                    servicer.get_ships,
                    request_deserializer=galaxy__pb2.GalacticPossition.FromString,
                    response_serializer=galaxy__pb2.Ship.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'ex01.Galaxy', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Galaxy(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def get_ships(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/ex01.Galaxy/get_ships',
            galaxy__pb2.GalacticPossition.SerializeToString,
            galaxy__pb2.Ship.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
