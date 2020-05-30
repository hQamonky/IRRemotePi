# FROM arm32v7/alpine:latest

# RUN apk add --no-cache --virtual .build-deps g++ python3-dev libffi-dev openssl-dev && \
#     apk add --no-cache --update python3 && \
#     apk add --no-cache py-pip && \
#     pip3 install --upgrade pip setuptools

FROM arm32v7/debian:latest

RUN apt update & apt upgrade -y
RUN apt install -y python3-dev
RUN pip3 install --upgrade setuptools


WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip3 install --no-cache-dir -r requirements.txt
RUN pip3 install --upgrade adafruit_blinka
RUN apt install -y libgpiod-dev
# RUN apk add --no-cache libgpiod-dev

COPY . .

CMD [ "python3", "./run.py" ]