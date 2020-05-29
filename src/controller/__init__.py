import src.controller.ir
from src.database import Database


class Controller:
    db = Database()

    # Database ---------------------------------------------------------------------------------------------------------
    def clear_database(self):
        self.db.create()
        return "Database cleared"

    # Devices ----------------------------------------------------------------------------------------------------------
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

    # Commands ---------------------------------------------------------------------------------------------------------
    def start_recording(self, device_id):
        # ir_read.resume()
        device = self.db.get_device(device_id)
        return device['name']

    def end_recording(self, device_id, command_name):
        # command = array.array(‘H’, [ir_read[x] for x in range(len(ir_read))])
        command = "test command"
        return self.db.new_command(command_name, device_id, command)

    def edit_command(self, device_id, command_id, new_name):
        return self.db.update_command(command_id, new_name)

    def delete_command(self, device_id, command_id):
        return self.db.delete_command(command_id)

    def send_command(self, device_id, command_id):
        command = self.db.get_command(command_id)
        device = self.db.get_device(device_id)
        print(command['name'] + " sent from " + device['name'] + ".")
        # ir.send(command)
        data = {
            "device": device,
            "command": command
        }
        return data
