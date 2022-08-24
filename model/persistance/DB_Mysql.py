import mysql.connector


class DB_Mysql:
    """Class to stablish connection to Mysql server using mysqlconnector
    """

    def __init__(self, host: str, username: str, password: str, database: str) -> None:
        """Constructor

        :param host: IP or domain
        :type host: str
        :param username: username for Mysql connection
        :type username: str
        :param password: password for Mysql connection
        :type password: str
        :param database: name of DB
        :type database: str
        """
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
        """Close the connection
        """
        self.cx.close()
