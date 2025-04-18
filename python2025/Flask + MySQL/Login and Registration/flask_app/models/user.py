from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re

class User:
    DB = "login_db"

    def __init__(self, data):
        self.id = data["id"]
        self.first_name = data["first_name"]
        self.last_name = data["last_name"]
        self.email = data["email"]
        self.password = data["password"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]

    @classmethod
    def create_user(cls, data):
        query = "INSERT INTO users (first_name, last_name, email, password) VALUES (%(first_name)s, %(last_name)s, %(email)s, %(password)s);"
        return connectToMySQL(cls.DB).query_db(query, data)

    @classmethod
    def get_by_email(cls, data):
        query = "SELECT * FROM users WHERE email = %(email)s;"
        results = connectToMySQL(cls.DB).query_db(query, data)
        return cls(results[0]) if results else None

    @classmethod
    def get_by_id(cls, data):
        query = "SELECT * FROM users WHERE id = %(id)s;"
        results = connectToMySQL(cls.DB).query_db(query, data)
        return cls(results[0]) if results else None

    @staticmethod
    def validate_registration(data):
        is_valid = True
        if len(data["first_name"]) < 2 or not data["first_name"].isalpha():
            flash("First name must be at least 2 letters and letters only.")
            is_valid = False
        if len(data["last_name"]) < 2 or not data["last_name"].isalpha():
            flash("Last name must be at least 2 letters and letters only.")
            is_valid = False
        if not re.match(r"[^@]+@[^@]+\.[^@]+", data["email"]):
            flash("Invalid email address.")
            is_valid = False
        if len(data["password"]) < 8:
            flash("Password must be at least 8 characters.")
            is_valid = False
        if data["password"] != data["confirm_password"]:
            flash("Passwords do not match.")
            is_valid = False
        return is_valid
