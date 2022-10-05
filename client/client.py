from flask import Flask

import grpc
import model_pb2
import model_pb2_grpc

app = Flask('end-to-end_ML_model_client')

img = 'some random image goes here'


# easy function to run the client and wait for a response:
@app.route('/')
def run_client():
    # we will use port 8888 to communicate between the client and server
    try:
        with grpc.insecure_channel('172.17.0.3:8888') as channel:
            stub = model_pb2_grpc.PredictorStub(channel)
            response = stub.PredictImage(model_pb2.ModelFeaturesRequest(processed_image=bytes(img, "utf-8")))

            # return response as cleaned html code
            response = bytes(str(response), "utf-8").decode("unicode_escape")
            print("Client received the following response:" + response)
            return "<h1>Client Received:</h1>" + response
    except Exception as e:
        return "<h1>ERROR</h1>" + str(e)


if __name__ == '__main__':
    # 5000 is the default port for Flask apps.
    app.run(host='0.0.0.0', port=5000)
