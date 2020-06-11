from src.controller.ir import IR
from src.database import Database


class Controller:
    db = Database()
    ir = {}

    def __init__(self):
        self.load_ir()

    # IR

    def load_ir(self):
        self.ir = {}
        self.db.clean_commands()
        devices = self.db.get_devices()
        for device in devices:
            self.ir['device_' + str(device['id'])] = IR(device['id'], device['gpio'], self.db.get_commands(device['id']))

    # Database

    def clear_database(self):
        self.db.create()
        self.load_ir()
        return "Database cleared"

    # Devices

    def get_devices(self):
        return self.db.get_devices()

    def new_device(self, device_name, gpio):
        device_id =  self.db.new_device(device_name, gpio)
        self.load_ir()
        return {
            "id": device_id,
            "name": device_name,
            "gpio": gpio,
            "commands": []
        }

    def get_device(self, device_id):
        device = self.db.get_device(device_id)
        device = {"name": device["name"], "gpio": device["gpio"], "commands": self.db.get_commands(device_id)}
        return device

    def edit_device(self, device_id, name, gpio):
        result = self.db.update_device(device_id, name, gpio)
        self.load_ir()
        return result

    def delete_device(self, device_id):
        result = self.db.delete_device(device_id)
        self.load_ir()
        return result

    # Commands

    def record_command(self, device_id, command_name):
        command_id = self.db.new_command(command_name, device_id, "new_command")
        signal = self.ir['device_' + str(device_id)].record(command_id)
        # Waiting for user input...
        self.db.update_command_signal(command_id, signal)
        self.db.clean_commands()
        return {
            "id": command_id,
            "device_id": device_id,
            "name": command_name,
            "signal": signal
        }

    def edit_command(self, device_id, command_id, new_name):
        return self.db.update_command_name(command_id, new_name)

    def delete_command(self, device_id, command_id):
        result = self.db.delete_command(command_id)
        self.load_ir()
        return result

    def send_command(self, device_id, command_id):
        command = self.db.get_command(command_id)
        device = self.db.get_device(device_id)
        self.ir['device_' + str(device_id)].send(command_id)
        data = {
            "device": device,
            "command": command
        }
        return data
