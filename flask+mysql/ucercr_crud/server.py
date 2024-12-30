from flask import Flask, render_template, request, redirect, url_for
from flask_mysqldb import MySQL
import datetime

app = Flask(__name__)

# Configure MySQL connection
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'   
app.config['MYSQL_PASSWORD'] = 'root'  
app.config['MYSQL_DB'] = 'users_schema'

mysql = MySQL(app)

@app.route('/users')
def show_users():
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT id, first_name, last_name, email, created_at, updated_at FROM users")
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

# Route to edit an existing user
@app.route('/users/edit/<int:user_id>', methods=['GET'])
def edit_user(user_id):
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM users WHERE id = %s", (user_id,))
    user = cursor.fetchone()
    cursor.close()
    return render_template('edit_user.html', user=user)

# Route to update the user's information
@app.route('/users/update/<int:user_id>', methods=['POST'])
def update_user(user_id):
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    updated_at = datetime.datetime.now()
    
    cursor = mysql.connection.cursor()
    cursor.execute(
        "UPDATE users SET first_name = %s, last_name = %s, updated_at = %s WHERE id = %s",
        (first_name, last_name, updated_at, user_id)
    )
    mysql.connection.commit()
    cursor.close()
    return redirect('/users')

# Route to show details of a specific user
@app.route('/users/show/<int:user_id>', methods=['GET'])
def show_user(user_id):
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM users WHERE id = %s", (user_id,))
    user = cursor.fetchone()
    cursor.close()
    return render_template('show_user.html', user=user)

# Route to delete a user
@app.route('/users/delete/<int:user_id>', methods=['GET'])
def delete_user(user_id):
    cursor = mysql.connection.cursor()
    cursor.execute("DELETE FROM users WHERE id = %s", (user_id,))
    mysql.connection.commit()
    cursor.close()
    return redirect('/users')


if __name__ == '__main__':
    app.run(debug=True)
