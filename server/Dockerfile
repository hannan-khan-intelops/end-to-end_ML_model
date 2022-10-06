# again, this image is about 2.5GB in size. We could actually reduce
# its size using a multi-stage dockerfile, or even just a smaller
# python/tensorflow image. The tensorflow library is what is taking
# the majority of the space.
FROM python:latest

WORKDIR /usr/src/app

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# need due to un-resolvable install conflicts betwee
# tf, grpcio-tools, and protobufs.
# This actually results in slower processing time.
# try not to use it.
ENV PROTOCOL_BUFFERS_PYTHON_IMPLEMENTATION=python

CMD python server.py