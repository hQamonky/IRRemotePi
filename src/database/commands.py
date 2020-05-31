class Commands:
    @staticmethod
    def create(cursor):
        cursor.execute("CREATE TABLE Commands ("
                       "id integer PRIMARY KEY AUTOINCREMENT, "
                       "device_id INTEGER, "
                       "name text, "
                       "signal text)")

    @staticmethod
    def drop(cursor):
        cursor.execute("DROP TABLE IF EXISTS Commands")

    @staticmethod
    def select_all(cursor):
        cursor.execute("SELECT * FROM Commands")
        return cursor.fetchall()

    @staticmethod
    def select_device(cursor, device_id):
        cursor.execute("SELECT * FROM Commands WHERE device_id = ?", (device_id,))
        return cursor.fetchall()

    @staticmethod
    def select(cursor, command_id):
        cursor.execute("SELECT * FROM Commands WHERE id = ?", (command_id,))
        return cursor.fetchall()

    @staticmethod
    def select_last_command_id(cursor):
        cursor.execute("SELECT id FROM Commands ORDER BY id DESC LIMIT 1")
        return cursor.fetchall()

    @staticmethod
    def insert(cursor, device_id, name, signal):
        cursor.execute("INSERT INTO Commands (device_id, name, signal) VALUES (?, ?, ?)",
                       (device_id, name, signal))

    @staticmethod
    def update_signal(cursor, identifier, signal):
        cursor.execute("UPDATE Commands SET signal = ? WHERE id = ?", (signal, identifier))

    @staticmethod
    def update_name(cursor, identifier, name):
        cursor.execute("UPDATE Commands SET name = ? WHERE id = ?", (name, identifier))

    @staticmethod
    def delete(cursor, identifier):
        cursor.execute("DELETE FROM Commands WHERE id = ?", (identifier,))

    @staticmethod
    def delete_device(cursor, device_id):
        cursor.execute("DELETE FROM Commands WHERE device_id = ?", (device_id,))

    @staticmethod
    def clean(cursor):
        cursor.execute("DELETE FROM Commands WHERE signal = new_command")
