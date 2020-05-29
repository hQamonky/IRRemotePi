class Devices:
    @staticmethod
    def create(cursor):
        cursor.execute("CREATE TABLE Devices (id integer PRIMARY KEY AUTOINCREMENT, name text UNIQUE)")

    @staticmethod
    def drop(cursor):
        cursor.execute("DROP TABLE IF EXISTS Devices")

    @staticmethod
    def select_all(cursor):
        cursor.execute("SELECT * FROM Devices")
        return cursor.fetchall()

    @staticmethod
    def select(cursor, identifier):
        cursor.execute("SELECT * FROM Devices WHERE id = ?", (identifier,))
        return cursor.fetchall()

    @staticmethod
    def insert(cursor, name):
        cursor.execute("INSERT INTO Devices (name) VALUES (?)", (name,))

    @staticmethod
    def update(cursor, device_id, new_name):
        cursor.execute("UPDATE Devices SET name = ? WHERE id = ?", (new_name, device_id))

    @staticmethod
    def delete(cursor, device_id):
        cursor.execute("DELETE FROM Devices WHERE id = ?", (device_id,))
