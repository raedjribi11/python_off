import pymysql.cursors

class MySQLConnection:
    def __init__(self, db):
        connection = pymysql.connect(
            host='localhost',
            user='root',
            password='root',  
            db=db,
            charset='utf8mb4',
            cursorclass=pymysql.cursors.DictCursor,
            autocommit=True
        )
        self.connection = connection

    def query_db(self, query, data=None):
        with self.connection.cursor() as cursor:
            try:
                cursor.execute(query, data)
                if query.lower().startswith("select"):
                    return cursor.fetchall()
                elif query.lower().startswith("insert"):
                    self.connection.commit()
                    return cursor.lastrowid
                else:
                    self.connection.commit()
            except Exception as e:
                print("Something went wrong", e)
                return False

def connectToMySQL(db):
    return MySQLConnection(db)
