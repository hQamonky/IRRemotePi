from ircodec.command import CommandSet
import json


class IR:
    controller = None
    name = None
    TR_pin = None  # Transmitter GPIO pin
    RR_pin = 13  # Receiver GPIO pin

    def __init__(self, device, gpio, commands):
        self.name = "device_" + str(device)
        self.TR_pin = gpio
        if not commands:
            self.controller = CommandSet(emitter_gpio=self.TR_pin, receiver_gpio=self.RR_pin, name=self.name)
        else:
            remote_json = json.dumps(self.build_json(commands))
            self.controller = CommandSet.from_json(remote_json)

    def build_json(self, commands):
        data = '{'
        for command in commands:
            data = data + '"command_' + str(command['id']) + '": ' + command['signal'] + ','
        data = data[:-1] + '}'
        return {
            "type": "CommandSet",
            "name": self.name,
            "emitter_gpio": self.TR_pin,
            "receiver_gpio": self.RR_pin,
            "commands": json.loads(data),
            "description": ""
        }

    def record(self, command):
        self.controller.add("command_" + str(command))
        return self.controller.commands["command_" + str(command)].to_json()

    def send(self, command):
        self.controller.emit("command_" + str(command))

    def get_id(self):
        return self.name[7:]
