import mysql.connector
from mysql.connector import Error

class MySQLConnection:
    def __init__(self, db_config):
        self.config = db_config
        self.connection = None

    def connect(self):
        try:
            self.connection = mysql.connector.connect(**self.config)
        except Error as e:
            print(f"Error connecting to MySQL: {e}")
    
    def query_db(self, query, data=None):
        cursor = self.connection.cursor(dictionary=True)
        try:
            if data:
                cursor.execute(query, data)
            else:
                cursor.execute(query)
            if query.lower().startswith("select"):
                return cursor.fetchall()
            self.connection.commit()
            return cursor.lastrowid
        except Error as e:
            print(f"Query Error: {e}")
            return False
        finally:
            cursor.close()

    def close(self):
        if self.connection:
            self.connection.close()
