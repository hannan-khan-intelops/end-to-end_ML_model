# since this is an example, lets not care about the container size.
# in production, your container size should be smaller than the
# 2.5GB behemoth this project produces.
FROM python:latest

WORKDIR /usr/src/app

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# we expose the port that will be used by our Flask app.
EXPOSE 5000

CMD python client.py