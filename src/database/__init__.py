import sqlite3
from src.database.devices import Devices
from src.database.commands import Commands

database = './src/irRemotePi.db'


def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d


class Database:
    connection = None

    def connect(self):
        self.connection = sqlite3.connect(database)
        # Convert data format to json
        self.connection.row_factory = dict_factory
        return self.connection.cursor()

    def close(self):
        # Save (commit) the changes
        self.connection.commit()
        # We can also close the connection if we are done with it.
        # Just be sure any changes have been committed or they will be lost.
        self.connection.close()

    # Creates the database. Warning : this will override the existing database.
    def create(self):
        c = self.connect()

        # Delete tables if exists
        Devices.drop(c)
        Commands.drop(c)

        # Create tables
        Devices.create(c)
        Commands.create(c)

        self.close()

    # Devices ----------------------------------------------------------------------------------------------------------

    def get_devices(self):
        data = Devices.select_all(self.connect())
        self.close()
        return data

    def new_device(self, name, gpio):
        Devices.insert(self.connect(), name, gpio)
        self.close()
        return "Device added"

    def get_device(self, device_id):
        data = Devices.select(self.connect(), device_id)
        self.close()
        return data[0]

    def update_device(self, device_id, new_name, gpio):
        Devices.update(self.connect(), device_id, new_name, gpio)
        self.close()
        return "Device updated"

    def delete_device(self, device_id):
        c = self.connect()
        # Delete commands from device
        Commands.delete_device(c, device_id)
        # Delete device
        Devices.delete(c, device_id)
        self.close()
        return "Device removed"

    # Commands ---------------------------------------------------------------------------------------------------------

    def get_all_commands(self):
        c = self.connect()
        data = Commands.select_all(c)
        self.close()
        return data

    def get_commands(self, device_id):
        c = self.connect()
        data = Commands.select_device(c, device_id)
        self.close()
        return data

    def get_command(self, command_id):
        c = self.connect()
        data = Commands.select(c, command_id)
        self.close()
        return data[0]

    def new_command(self, name, device_id, signal):
        c = self.connect()
        Commands.insert(c, device_id, name, signal)
        new_command_id = Commands.select_last_command_id(c)
        self.close()
        return new_command_id[0]['id']

    def update_command_signal(self, command_id, signal):
        Commands.update_signal(self.connect(), command_id, signal)
        self.close()
        return "Command updated"

    def update_command_name(self, command_id, new_name):
        Commands.update_name(self.connect(), command_id, new_name)
        self.close()
        return "Command updated"

    def delete_command(self, command_id):
        Commands.delete(self.connect(), command_id)
        self.close()
        return "Command removed"

    def clean_commands(self):
        Commands.clean(self.connect())
        self.close()
        return "Cleaned commands"
