import sqlite3

class DbManager:

    def __init__(self):
        self.__name = "quanlysinhvien.db"
        self.conn = None
        self.cursor = None

    def open_connection(self):
        self.conn = sqlite3.connect(self.__name)
        self.cursor = self.conn.cursor()

    def close_connection(self):
        if self.conn is not None:
            self.conn.close()

    def create_tables(self):
        self.open_connection()
        self.cursor.execute("CREATE TABLE IF NOT EXISTS users ("
                            "id INTEGER PRIMARY KEY AUTOINCREMENT,"
                            "username TEXT NOT NULL,"
                            "password TEXT NOT NULL)")

        self.cursor.execute("CREATE TABLE IF NOT EXISTS admins("
                            "id INTEGER PRIMARY KEY AUTOINCREMENT,"
                            "user_id INTEGER NOT NULL,"
                            "role INTEGER NOT NULL,"
                            "FOREIGN KEY(user_id) REFERENCES users(id))")

        self.cursor.execute("CREATE TABLE IF NOT EXISTS members("
                            "id INTEGER PRIMARY KEY AUTOINCREMENT,"
                            "user_id INTEGER NOT NULL,"
                            "type INTEGER NOT NULL,"
                            "FOREIGN KEY(user_id) REFERENCES users(id))")

        self.conn.commit()
        self.close_connection()

