from flask import Flask, render_template, request, redirect
from flask_mysqldb import MySQL
import datetime

app = Flask(__name__)

# Configure MySQL connection
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'  # Replace with your MySQL username
app.config['MYSQL_PASSWORD'] = 'root'  # Replace with your MySQL password
app.config['MYSQL_DB'] = 'users_schema'

mysql = MySQL(app)

# Route to display all users
@app.route('/users')
def show_users():
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM users")
    all_users = cursor.fetchall()
    cursor.close()
    return render_template('read_all.html', users=all_users)

# Route to render the Add User form
@app.route('/users/new')
def new_user():
    return render_template('create.html')

# Route to add a new user
@app.route('/users/add', methods=['POST'])
def add_user():
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    created_at = datetime.datetime.now()
    updated_at = datetime.datetime.now()
    
    cursor = mysql.connection.cursor()
    cursor.execute(
        "INSERT INTO users (first_name, last_name, created_at, updated_at) VALUES (%s, %s, %s, %s)",
        (first_name, last_name, created_at, updated_at)
    )
    mysql.connection.commit()
    cursor.close()
    return redirect('/users')

if __name__ == '__main__':
    app.run(debug=True)
