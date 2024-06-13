from DbManager import DbManager
from User import User

IS_ADMIN = False

class Admin(User):
    def __init__(self, username, password, role=0):
        super().__init__(username, password)
        self.role = role
        self.is_admin = False  # Default to not admin

    def register(self):
        super().register()
        db = DbManager()
        db.open_connection()
        db.cursor.execute("INSERT INTO admins(user_id, role) VALUES (?,?)", (self.id, self.role))
        db.conn.commit()
        self.id = db.cursor.lastrowid
        db.close_connection()
        print("Admin registered, id =", self.id)

    def get_info(self):
        db = DbManager()
        db.open_connection()
        output = db.cursor.execute("SELECT * FROM admins WHERE user_id=?", (self.id,)).fetchone()
        db.close_connection()
        if output is not None:
            return output
        else:
            return None


    def login(self):
        super().login()
        if self.logged_in:
            db = DbManager()
            db.open_connection()
            output = db.cursor.execute("SELECT * FROM admins WHERE user_id=?", (self.id,)).fetchone()
            db.close_connection()
            if output is not None:
                self.role = output[2]  # Lấy role từ cột thứ 3 trong kết quả trả về
                print("Admin role = ", self.role)
                self.is_admin = True  # Nếu người dùng là admin, đặt is_admin = True
            else:
                print("Admin role not registered")
                self.is_admin = False

    def get_all_admins(self):
        db = DbManager()
        db.open_connection()
        output = db.cursor.execute("SELECT * FROM admins").fetchall()
        db.close_connection()
        return output

    def delete_all_admins(self):
        db = DbManager()
        db.open_connection()
        db.cursor.execute("DELETE FROM admins")
        db.conn.commit()
        db.close_connection()
