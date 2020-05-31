from src.controller.ir import IR
from src.database import Database


class Controller:
    db = Database()
    db.clean_commands()
    ir = IR(db.get_all_commands())

    # Database

    def clear_database(self):
        self.db.create()
        return "Database cleared"

    # Devices

    def get_devices(self):
        return self.db.get_devices()

    def new_device(self, device):
        return self.db.new_device(device)

    def get_device(self, device_id):
        device = self.db.get_device(device_id)
        device = {"name": device["name"], "commands": self.db.get_commands(device_id)}
        return device

    def edit_device(self, device_id, new_name):
        return self.db.update_device(device_id, new_name)

    def delete_device(self, device_id):
        return self.db.delete_device(device_id)

    # Commands

    def record_command(self, device_id, command_name):
        command_id = self.db.new_command(command_name, device_id, "new_command")
        signal = self.ir.record(command_id)
        # Waiting for user input...
        self.db.update_command_signal(command_id, signal)
        self.db.clean_commands()
        return "Command added"

    def edit_command(self, device_id, command_id, new_name):
        return self.db.update_command_name(command_id, new_name)

    def delete_command(self, device_id, command_id):
        return self.db.delete_command(command_id)

    def send_command(self, device_id, command_id):
        command = self.db.get_command(command_id)
        device = self.db.get_device(device_id)
        self.ir.send(command_id)
        print(command['name'] + " sent from " + device['name'] + ".")
        data = {
            "device": device,
            "command": command
        }
        return data
