from concurrent import futures
import grpc
import model_pb2
import model_pb2_grpc
import socket
import tensorflow as tf
from tensorflow import keras


def normalize_img(image):
    """Turns each value of the image to make it between
    0 and 255."""
    return tf.cast(image, tf.float32) / 255.0


def load_image(image_bytes):
    """Loads image from bytes and preprocesses it.
    Only the image array is loaded using the decode_raw function.
    Converting to image from bytes is a hassle using Pillow."""
    image_tensor = tf.io.decode_raw(image_bytes, tf.uint8)
    image_tensor = tf.reshape(image_tensor, [1, 28, 28])
    image_tensor = normalize_img(image_tensor)
    return image_tensor


def predict(image_bytes):
    """Loads the model, the image, and performs prediction.
    Then returns the guess as well as its confidence."""
    model = keras.models.load_model('mnist_model')
    image = load_image(image_bytes)
    result = model.predict(image)[0]
    print("All prediction results", result)
    return result.argmax(), result[result.argmax()] * 100


class Predictor(model_pb2_grpc.PredictorServicer):
    def PredictImage(self, request, context):
        # predict the image
        guess, confidence = predict(image_bytes=request.image)
        print(f"Server guess {guess}, confidence {confidence}")
        # return the response message
        return model_pb2.ModelOutputResponse(guess=int(guess), confidence=float(confidence))


def serve():
    print("Server Running...")
    # creates a server
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    # adds our PredictorService object to our server.
    model_pb2_grpc.add_PredictorServicer_to_server(Predictor(), server)
    # adds the same port that our client connects to.
    server.add_insecure_port('[::]:9999')
    # we print out where our server is running,
    # to be able to set up our client code correctly.
    print("Server located at: ", end='')
    print(socket.gethostbyname(socket.gethostname()))
    # starts the server
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    serve()
