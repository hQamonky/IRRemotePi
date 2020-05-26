import src.controller.ir
import src.database


class Controller:
    # Devices ----------------------------------------------------------------------------------------------------------
    def get_devices(self):
        return

    def new_device(self, device):
        return

    def get_device(self, device):
        return

    def edit_device(self, device, new_name):
        return

    def delete_device(self, device):
        return

    # Commands ---------------------------------------------------------------------------------------------------------
    def get_commands(self, device):
        return

    def start_recording(self):
        # ir_read.resume()
        return

    def end_recording(self, device, command_name):
        # command = array.array(‘H’, [ir_read[x] for x in range(len(ir_read))])
        return

    def get_command(self, device, command_name):
        return

    def edit_command(self, device, command_name, new_name):
        return

    def delete_command(self, device, command_name):
        return

    def send_command(self, device, command_name):
        return
