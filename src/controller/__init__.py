from src.controller.ir import IR
from src.database import Database


class Controller:
    db = Database()
    ir = IR()

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

    def start_recording(self, device_id):
        self.ir.start_recording()
        device = self.db.get_device(device_id)
        return device['name']

    def end_recording(self, device_id, command_name):
        signal = self.ir.stop_recording()
        # signal = "test signal"
        print(signal)
        return self.db.new_command(command_name, device_id, str(signal))

    def edit_command(self, device_id, command_id, new_name):
        return self.db.update_command(command_id, new_name)

    def delete_command(self, device_id, command_id):
        return self.db.delete_command(command_id)

    def send_command(self, device_id, command_id):
        command = self.db.get_command(command_id)
        device = self.db.get_device(device_id)
        print(command['name'] + " sent from " + device['name'] + ".")
        self.ir.send(command['signal'])
        data = {
            "device": device,
            "command": command
        }
        return data
