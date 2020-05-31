FROM arm32v7/alpine:latest

RUN apk add --no-cache --virtual .build-deps g++ python3-dev libffi-dev openssl-dev && \
    apk add --no-cache --update python3 && \
    apk add --no-cache py-pip && \
    pip3 install --upgrade pip setuptools


WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip3 install --no-cache-dir -r requirements.txt
RUN pip3 install --upgrade adafruit_blinka
RUN apk add --no-cache gpiod libgpiod-dev


# FROM arm32v7/python:3
#
# WORKDIR /usr/src/app
#
# COPY requirements.txt ./
# RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD [ "python3", "./run.py" ]