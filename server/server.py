from concurrent import futures
import grpc
import model_pb2
import model_pb2_grpc
import socket
import tensorflow as tf
import tensorflow_datasets as tfds


def normalize_img(image):
    """Normalizes images: `uint8` -> `float32`."""
    return tf.cast(image, tf.float32) / 255.0


def load_model():
    ...


def predict(image):
    model = load_model()
    ...
    return 0, 0


class Predictor(model_pb2_grpc.PredictorServicer):
    def PredictImage(self, request, context):
        # convert bytes to float array
        image = ...
        # normalize the image
        image = normalize_img(image)
        # predict the image
        guess, confidence = predict(image)
        # return the response message
        return model_pb2.ModelOutputResponse(guess=int(guess), confidence=float(confidence))


def serve():
    print("Server Running...")
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    model_pb2_grpc.add_PredictorServicer_to_server(Predictor(), server)
    server.add_insecure_port('[::]:8888')
    # we print out where our server is running,
    # to be able to set up our client correctly.
    print("Server located at: ", end='')
    print(socket.gethostbyname(socket.gethostname()))
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    serve()
