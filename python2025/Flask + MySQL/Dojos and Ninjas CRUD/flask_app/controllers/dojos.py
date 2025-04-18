from flask import render_template, request, redirect
from flask_app import app
from flask_app.models.dojo import Dojo

@app.route("/dojos")
def dojos():
    return render_template("dojos.html", dojos=Dojo.get_all())

@app.route("/dojos/create", methods=["POST"])
def create_dojo():
    Dojo.save(request.form)
    return redirect("/dojos")

@app.route("/dojos/<int:id>")
def show_dojo(id):
    return render_template("dojo_show.html", dojo=Dojo.get_one_with_ninjas({"id": id}))
