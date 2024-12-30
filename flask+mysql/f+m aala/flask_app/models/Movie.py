from flask_app.config.mysqlconnection import DB,connectToMySQL

class Movie :
    def __init__(self , data):
        self.id = data['id']
        self.title = data['title']
        self.genre = data['genre']
        self.discription = data['discription']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM movies;"
        result = connectToMySQL(DB).query_db(query)
    
""""
result=
(
    {
        'id':1,
        'title':"saw",
        'genre':"horror",
        'discription':"creepy looking doll",
        'created_at':"12-12-2021",
        'updated_at':""11-12-2021",
    }
    ,
    {
        'id':2,
        'title':"spider-man",
        'genre':"fun",
        'discription':"  advanture",
        'created_at':"12-12-2021",
        'updated_at':""11-12-2021",
    }
)