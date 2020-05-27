import src.controller.ir
from src.database import Database


class Controller:
    db = Database()

    # Database ---------------------------------------------------------------------------------------------------------
    def clear_database(self):
        self.db.create()
        return "Database created"

    # Devices ----------------------------------------------------------------------------------------------------------
    def get_devices(self):
        return self.db.get_devices()

    def new_device(self, device):
        return self.db.new_device(device)

    def get_device(self, device):
        device = {"name": device, "commands": self.db.get_commands(device)}
        return device

    def edit_device(self, device, new_name):
        return self.db.update_device(device, new_name)

    def delete_device(self, device):
        return self.db.delete_device(device)

    # Commands ---------------------------------------------------------------------------------------------------------
    def edit_command(self, device, command_name, new_name):
        return

    def delete_command(self, device, command_name):
        return

    def start_recording(self):
        # ir_read.resume()
        return

    def end_recording(self, device, command_name):
        # command = array.array(‘H’, [ir_read[x] for x in range(len(ir_read))])
        return

    def send_command(self, device, command_name):
        return
