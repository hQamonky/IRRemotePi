FROM arm32v7/alpine:latest
# FROM arm32v7/python:3

RUN apk add --no-cache python3-dev

# Fix and upgrade pip3
COPY fix_pip3_upgrade.sh ./
RUN chmod +x ./fix_pip3_upgrade.sh
RUN ./fix_pip3_upgrade.sh
# RUN if [ ! -e /usr/bin/pip ]; then ln -s pip3 /usr/bin/pip ; fi && \
#     if [[ ! -e /usr/bin/python ]]; then ln -sf /usr/bin/python3 /usr/bin/python; fi && \
RUN pip3 install --upgrade pip

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
RUN apk add --no-cache libgpiod-dev

COPY . .

CMD [ "python3", "./run.py" ]