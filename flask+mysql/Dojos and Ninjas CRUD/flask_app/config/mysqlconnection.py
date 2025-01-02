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
                query = cursor.mogrify(query, data)
                cursor.execute(query)
                if query.lower().startswith('select'):
                    return cursor.fetchall()
                else:
                    self.connection.commit()
                    return cursor.lastrowid
            except Exception as e:
                print("Something went wrong:", e)
                return None

def connectToMySQL(db):
    return MySQLConnection(db)
