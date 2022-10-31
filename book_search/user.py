from sqlite3 import Connection


class User:
    def __init__(self, conn: Connection) -> None:
        self.conn = conn
        self.cursor = conn.cursor()

    def create_user(self):
        self.cursor.execute(
            "CREATE TABLE IF NOT EXISTS userstable(username TEXT,password TEXT)"
        )

    def add_user(self, username, password):
        self.cursor.execute(
            "INSERT INTO userstable(username,password) VALUES (?,?)",
            (username, password),
        )
        self.conn.commit()

    def login_user(self, username, password):
        self.cursor.execute(
            "SELECT * FROM userstable WHERE username =? AND password = ?",
            (username, password),
        )
        data = self.cursor.fetchall()
        return data
