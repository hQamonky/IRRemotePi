FROM arm32v7/alpine:latest
# FROM arm32v7/python:3

# RUN apk add --no-cache python3-dev \
#     && apk add --no-cache py-pip \
#     && pip3 install --upgrade pip
RUN apk add --no-cache --virtual .build-deps g++ python3-dev libffi-dev openssl-dev && \
    apk add --no-cache --update python3 && \
    apk add --no-cache py-pip && \
    pip3 install --upgrade pip setuptools

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
RUN apk add --no-cache libgpiod-dev

COPY . .

CMD [ "python3", "./run.py" ]