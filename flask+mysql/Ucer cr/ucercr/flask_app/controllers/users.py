from flask import Flask, render_template, redirect, request
from flask_app.models.user import User

app = Flask(__name__)

@app.route('/')
def read_all():
    users = User.get_all()
    return render_template('read_all.html', users=users)

@app.route('/create_user', methods=['GET', 'POST'])
def create_user():
    if request.method == 'POST':
        data = {
            "first_name": request.form['first_name'],
            "last_name": request.form['last_name'],
            "email": request.form['email']
        }
        User.create(data)
        return redirect('/')
    return render_template('create_user.html')
