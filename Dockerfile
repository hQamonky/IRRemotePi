FROM arm32v7/alpine:latest
# FROM arm32v7/python:3

RUN apk add --no-cache python3-dev \
    && apk add --no-cache  \
    && pip3 install --upgrade pip

COPY fix_pip3_upgrade.sh ./
RUN chmod +x ./fix_pip3_upgrade.sh
RUN ./fix_pip3_upgrade.sh

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
RUN apk add --no-cache libgpiod-dev

COPY . .

CMD [ "python3", "./run.py" ]