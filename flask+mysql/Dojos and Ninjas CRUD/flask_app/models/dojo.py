from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.ninja import Ninja

class Dojo:
    DB = "dojos_and_ninjas"

    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.ninjas = []

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM dojos;"
        results = connectToMySQL(cls.DB).query_db(query)
        return [cls(dojo) for dojo in results]

    @classmethod
    def save(cls, data):
        query = "INSERT INTO dojos (name) VALUES (%(name)s);"
        return connectToMySQL(cls.DB).query_db(query, data)

    @classmethod
    def get_one_with_ninjas(cls, data):
        query = """
            SELECT * FROM dojos
            LEFT JOIN ninjas ON dojos.id = ninjas.dojo_id
            WHERE dojos.id = %(id)s;
        """
        results = connectToMySQL(cls.DB).query_db(query, data)

        if results:
            dojo = cls(results[0])
            for row in results:
                if row['ninjas.id']:
                    ninja_data = {
                        'id': row['ninjas.id'],
                        'first_name': row['first_name'],
                        'last_name': row['last_name'],
                        'age': row['age'],
                        'dojo_id': row['dojo_id'],
                        'created_at': row['ninjas.created_at'],
                        'updated_at': row['ninjas.updated_at']
                    }
                    dojo.ninjas.append(Ninja(ninja_data))
            return dojo
        return None
