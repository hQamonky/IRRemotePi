class Devices:
    @staticmethod
    def create(cursor):
        cursor.execute("CREATE TABLE Devices (id text PRIMARY KEY AUTOINCREMENT, name text UNIQUE)")

    @staticmethod
    def drop(cursor):
        cursor.execute("DROP TABLE IF EXISTS Devices")

    @staticmethod
    def select_all(cursor):
        cursor.execute("SELECT * FROM Devices")
        return cursor.fetchall()

    @staticmethod
    def select_id(cursor, name):
        cursor.execute("SELECT id FROM Devices WHERE name = ?", (name,))
        return cursor.fetchall()

    @staticmethod
    def insert(cursor, name):
        cursor.execute("INSERT INTO Devices VALUES ?", (name,))

    @staticmethod
    def update(cursor, device_name, new_name):
        cursor.execute("UPDATE Devices SET name = ? WHERE name = ?", (new_name, device_name))

    @staticmethod
    def delete(cursor, name):
        cursor.execute("DELETE FROM Devices WHERE name = ?", (name,))
