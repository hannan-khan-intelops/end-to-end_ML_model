# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import model_pb2 as model__pb2


class PredictorStub(object):
    """this is the service to call for the model."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.PredictImage = channel.unary_unary(
            "/model.Predictor/PredictImage",
            request_serializer=model__pb2.ModelFeaturesRequest.SerializeToString,
            response_deserializer=model__pb2.ModelOutputResponse.FromString,
        )


class PredictorServicer(object):
    """this is the service to call for the model."""

    def PredictImage(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")


def add_PredictorServicer_to_server(servicer, server):
    rpc_method_handlers = {
        "PredictImage": grpc.unary_unary_rpc_method_handler(
            servicer.PredictImage,
            request_deserializer=model__pb2.ModelFeaturesRequest.FromString,
            response_serializer=model__pb2.ModelOutputResponse.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        "model.Predictor", rpc_method_handlers
    )
    server.add_generic_rpc_handlers((generic_handler,))


# This class is part of an EXPERIMENTAL API.
class Predictor(object):
    """this is the service to call for the model."""

    @staticmethod
    def PredictImage(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/model.Predictor/PredictImage",
            model__pb2.ModelFeaturesRequest.SerializeToString,
            model__pb2.ModelOutputResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )
