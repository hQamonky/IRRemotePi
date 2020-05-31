# import RPi.GPIO as GPIO
import pigpio
import array
import time
from ircodec.command import CommandSet
import subprocess
import json

# Making sure pigpio daemon is started
# subprocess.run(["sudo", "pigpiod"], check=True, stdout=subprocess.PIPE, universal_newlines=True)


class IR:
    controller = None
    TR_pin = 12  # Transmitter GPIO pin
    RR_pin = 13  # Receiver GPIO pin

    def __init__(self, commands):
        if not commands:
            self.controller = CommandSet(emitter_gpio=self.TR_pin, receiver_gpio=self.RR_pin, name='remote')
        else:
            remote_json = json.dumps(self.build_json(commands))
            print(remote_json)
            self.controller = CommandSet.from_json(remote_json)

    def build_json(self, commands):
        data = []
        for command in commands:
            command = '"' + str(command['id']) + '": ' + command['signal']
            print(command)
            data.append(json.loads(command))
        print("comnmands OK")
        return {
            "type": "CommandSet",
            "name": "remote",
            "emitter_gpio": str(self.TR_pin),
            "receiver_gpio": str(self.RR_pin),
            "commands": data,
            "description": ""
        }

    def record(self, command):
        self.controller.add(command)
        return self.controller.commands[command].to_json()

    def send(self, command):
        self.controller.emit(command)
