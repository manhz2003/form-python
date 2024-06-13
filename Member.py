from DbManager import DbManager
from User import User

class Member(User):
    def __init__(self, username, password, type=0):
        super().__init__(username, password)
        self.type = type

    def register(self):
        super().register()
        db = DbManager()
        db.open_connection()
        db.cursor.execute("INSERT INTO members(user_id, type) VALUES (?,?)", (self.id, self.type))
        db.conn.commit()
        self.id = db.cursor.lastrowid
        db.close_connection()
        print("Member registered, id =", self.id)

    def login(self):
        super().login()
        if self.logged_in:
            db = DbManager()
            db.open_connection()
            result = db.cursor.execute("SELECT * FROM members WHERE user_id=?", (self.id,)).fetchone()
            db.close_connection()
            if result:
                self.type = result[2]
                print(f"Member logged in. Type: {self.type}")
                return True
            else:
                print("Member type not registered")
        return False

    @staticmethod
    def get_members():
        db = DbManager()
        db.open_connection()
        members = db.cursor.execute("SELECT t1.id,t1.user_id,t2.username,t1.type "
                                    "FROM members t1,users t2 "
                                    "WHERE t1.user_id=t2.id ORDER BY t2.username").fetchall()
        db.close_connection()
        return members
