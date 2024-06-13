from DbManager import DbManager
class User(object):

    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.id = 0
        self.logged_in = False

    def register(self):
        db = DbManager()
        db.open_connection()
        db.cursor.execute("INSERT INTO users (username, password) VALUES (?,?)",
                                 (self.username, self.password))
        self.id = db.cursor.lastrowid
        db.conn.commit()
        db.close_connection()
        print(F"User registered successfully, id={self.id}")

    def login(self):
        db = DbManager()
        db.open_connection()
        output = db.cursor.execute("SELECT id FROM users WHERE username = ? AND password = ?",
                          (self.username, self.password)).fetchone()
        if output is not None:
            self.id = output[0]
            self.logged_in = True
            print(F"Logged in")
        else:
            self.logged_in = False
            print(F"Invalid username or password")
        db.close_connection()

    def logout(self):
        self.logged_in = False
        print(F"Logged out")