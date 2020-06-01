class Devices:
    @staticmethod
    def create(cursor):
        cursor.execute("CREATE TABLE Devices (id integer PRIMARY KEY AUTOINCREMENT, name text UNIQUE, gpio integer)")

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
    def insert(cursor, name, gpio):
        cursor.execute("INSERT INTO Devices (name, gpio) VALUES (?, ?)", (name, gpio))

    @staticmethod
    def update(cursor, device_id, name, gpio):
        cursor.execute("UPDATE Devices SET name = ?, gpio = ? WHERE id = ?", (name, gpio, device_id))

    @staticmethod
    def delete(cursor, device_id):
        cursor.execute("DELETE FROM Devices WHERE id = ?", (device_id,))
