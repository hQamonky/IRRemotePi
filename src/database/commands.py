class Commands:
    @staticmethod
    def create(cursor):
        cursor.execute("CREATE TABLE Commands ("
                       "id text PRIMARY KEY AUTOINCREMENT, "
                       "device_id INTEGER, "
                       "name text, "
                       "command text)")

    @staticmethod
    def drop(cursor):
        cursor.execute("DROP TABLE IF EXISTS Commands")

    @staticmethod
    def select(cursor, device_id):
        cursor.execute("SELECT * FROM Commands WHERE device_id = ?", (device_id,))
        return cursor.fetchall()

    @staticmethod
    def insert(cursor, device_id, name, command):
        cursor.execute("INSERT INTO Commands VALUES (?, ?, ?)",
                       (device_id, name, command))

    @staticmethod
    def update(cursor, identifier, name):
        cursor.execute("UPDATE Commands SET name = ? WHERE id = ?", (name, identifier))

    @staticmethod
    def delete(cursor, identifier):
        cursor.execute("DELETE FROM Commands WHERE id = ?", (identifier,))

    @staticmethod
    def delete_device(cursor, device_id):
        cursor.execute("DELETE FROM Commands WHERE device_id = ?", (device_id,))
