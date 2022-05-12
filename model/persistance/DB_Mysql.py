import mysql.connector

class DB_Mysql:
    def __init__(self, host: str, username: str, password: str, database: str) -> None:
        self.host = host
        self.username = username
        self.password = password
        self.database = database
        try:
            self.cx = mysql.connector.connect(user=self.username,
            password=self.password, 
            host=self.host,
            database=self.database)
        except mysql.connector.Error as err:
            print(err)        
            
    def close(self) -> None:
        self.cx.close()