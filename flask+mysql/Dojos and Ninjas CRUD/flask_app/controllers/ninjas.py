from flask import render_template, request, redirect
from flask_app import app
from flask_app.models.ninja import Ninja
from flask_app.models.dojo import Dojo

@app.route('/ninjas/new')
def new_ninja():
    return render_template('new_ninja.html', dojos=Dojo.get_all())

@app.route('/ninjas/create', methods=['POST'])
def create_ninja():
    Ninja.save({
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'age': request.form['age'],
        'dojo_id': request.form['dojo_id']
    })
    return redirect(f"/dojos/{request.form['dojo_id']}")
