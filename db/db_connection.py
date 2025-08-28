import sqlite3

class Database:
    def __init__(self, db_path="database.db"):
        self.conn = sqlite3.connect(db_path)

    def execute(self, query, params=()):
        cursor = self.conn.execute(query, params)
        self.conn.commit()
        return cursor

    def fetchall(self, query, params=()):
        return self.conn.execute(query, params).fetchall()

    def close(self):
        self.conn.close()
