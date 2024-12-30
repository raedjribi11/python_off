from flask import Flask, render_template, request, redirect
from mysqlconnection import MySQLConnection

app = Flask(__name__)

# Configure MySQL
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'yourpassword',
    'database': 'users_schema'
}
db = MySQLConnection(db_config)

@app.route('/users', methods=['GET'])
def read_all_users():
    query = "SELECT * FROM users"
    users = db.query_db(query)
    return render_template('read_all.html', users=users)

@app.route('/users/new', methods=['GET'])
def create_user_form():
    return render_template('create_user.html')

@app.route('/users/new', methods=['POST'])
def create_user():
    query = "INSERT INTO users (first_name, last_name, email) VALUES (%s, %s, %s)"
    data = (request.form['first_name'], request.form['last_name'], request.form['email'])
    db.query_db(query, data)
    return redirect('/users')

if __name__ == '__main__':
    app.run(debug=True)
