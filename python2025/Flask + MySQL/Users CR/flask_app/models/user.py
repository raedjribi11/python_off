from flask_app.config.mysqlconnection import connectToMySQL

class User:
    db = "users_schema"

    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users;"
        results = connectToMySQL(cls.db).query_db(query)
        return [cls(user) for user in results]

    @classmethod
    def save(cls, data):
        query = """
        INSERT INTO users (first_name, last_name, email)
        VALUES (%(first_name)s, %(last_name)s, %(email)s);
        """
        return connectToMySQL(cls.db).query_db(query, data)
