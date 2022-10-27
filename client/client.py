from flask import Flask
from PIL import Image

import grpc
import model_pb2
import model_pb2_grpc

app = Flask("end-to-end_ML_model_client")


@app.route('/')
def run_client():
    # we will use port 8888 to communicate between the client and server
    try:
        # replace the '172.17.0.2' with whatever your server prints out.
        # we create a channel for the stub to communicate with.
        with grpc.insecure_channel("172.17.0.2:9999") as channel:
            # we create a stub object that uses the channel
            stub = model_pb2_grpc.PredictorStub(channel)
            # in reality, this image would be retrieved from a database using another api.
            # (if we were coding according to OpenAPI standards).
            # The 'L' below stands for a one-channel (grayscale) image.
            # we open the image, and convert it bytes.
            bytes_string = Image.open("mnist_image_png.png").tobytes("raw", "L")
            response = stub.PredictImage(
                model_pb2.ModelFeaturesRequest(image=bytes_string)
            )
            # return response as terminal output and cleaned html code
            print("Client received the following response:" + str(response))
            return f"""<h1>Client Received:</h1>
            <h2>Guess: '{str(response.guess)}'</h2>
            <h2>Confidence: {response.confidence:.3f}%</h2>"""
    except Exception as e:
        # if there is any error, we have a way to handle for it here.
        return "<h1>ERROR</h1>" + str(e)


if __name__ == "__main__":
    # 5000 is the default port for Flask apps.
    # this port needs to be exposed in our dockerfile.
    app.run(host="0.0.0.0", port=5000)
