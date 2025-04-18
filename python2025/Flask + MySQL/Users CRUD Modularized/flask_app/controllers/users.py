from flask import render_template, request, redirect
from flask_app import app
from flask_app.models.user import User

@app.route("/")
@app.route("/users")
def index():
    users = User.get_all()
    return render_template("index.html", users=users)

@app.route("/users/new")
def new_user():
    return render_template("new_user.html")

@app.route("/users/create", methods=["POST"])
def create_user():
    User.create(request.form)
    return redirect("/users")

@app.route("/users/<int:id>")
def show_user(id):
    user = User.get_one({"id": id})
    return render_template("show_user.html", user=user)

@app.route("/users/<int:id>/edit")
def edit_user(id):
    user = User.get_one({"id": id})
    return render_template("edit_user.html", user=user)

@app.route("/users/<int:id>/update", methods=["POST"])
def update_user(id):
    data = {
        "id": id,
        "first_name": request.form["first_name"],
        "last_name": request.form["last_name"],
        "email": request.form["email"]
    }
    User.update(data)
    return redirect("/users")

@app.route("/users/<int:id>/delete", methods=["POST"])
def delete_user(id):
    User.delete({"id": id})
    return redirect("/users")
