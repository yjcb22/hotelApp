import sqlite3

class DB_Sqlite:
    def __init__(self, path: str) -> None:
        self.cx = sqlite3.connect(path)

    def close(self) -> None:
        self.cx.close()