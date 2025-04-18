from flask import render_template, request, redirect, session, flash
from flask_app import app
from flask_app.models.user import User
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt(app)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/register", methods=["POST"])
def register():
    if not User.validate_registration(request.form):
        return redirect("/")
    pw_hash = bcrypt.generate_password_hash(request.form['password'])
    data = {
        "first_name": request.form["first_name"],
        "last_name": request.form["last_name"],
        "email": request.form["email"],
        "password": pw_hash
    }
    user_id = User.create_user(data)
    session["user_id"] = user_id
    return redirect("/success")

@app.route("/login", methods=["POST"])
def login():
    user = User.get_by_email({"email": request.form["email"]})
    if not user or not bcrypt.check_password_hash(user.password, request.form["password"]):
        flash("Invalid email or password")
        return redirect("/")
    session["user_id"] = user.id
    return redirect("/success")

@app.route("/success")
def success():
    if "user_id" not in session:
        return redirect("/")
    return render_template("success.html", user=User.get_by_id({"id": session["user_id"]}))

@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")
