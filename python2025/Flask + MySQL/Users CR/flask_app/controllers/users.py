from flask_app import app
from flask import render_template, redirect, request
from flask_app.models.user import User

@app.route("/users")
def users():
    all_users = User.get_all()
    return render_template("read_all.html", users=all_users)

@app.route("/users/new")
def new_user():
    return render_template("create_user.html")

@app.route("/users/create", methods=["POST"])
def create_user():
    User.save(request.form)
    return redirect("/users")
