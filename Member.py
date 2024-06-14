from DbManager import DbManager
class Member:
    def __init__(self, username, password, type=0):
        self.username = username
        self.password = password
        self.type = type
        self.id = None  # Initialize ID

    def register(self):
        db = DbManager()
        db.open_connection()
        # Insert into users table first to get the user_id
        db.cursor.execute("INSERT INTO users(username, password) VALUES (?, ?)",
                          (self.username, self.password))
        db.conn.commit()
        self.user_id = db.cursor.lastrowid

        # Then insert into members table using the obtained user_id
        db.cursor.execute("INSERT INTO members(user_id, type) VALUES (?, ?)",
                          (self.user_id, self.type))
        db.conn.commit()
        self.id = db.cursor.lastrowid
        db.close_connection()

    @staticmethod
    def get_members():
        db = DbManager()
        db.open_connection()
        members = db.cursor.execute("SELECT members.id, users.username, members.type "
                                    "FROM members "
                                    "INNER JOIN users ON members.user_id = users.id "
                                    "ORDER BY members.id ASC").fetchall()
        db.close_connection()
        return members

    @staticmethod
    def search_members(username):
        db = DbManager()
        db.open_connection()
        members = db.cursor.execute("SELECT members.id, users.username, members.type "
                                    "FROM members "
                                    "INNER JOIN users ON members.user_id = users.id "
                                    "WHERE users.username LIKE ? "
                                    "ORDER BY members.id ASC", ('%' + username + '%',)).fetchall()
        db.close_connection()
        return members
