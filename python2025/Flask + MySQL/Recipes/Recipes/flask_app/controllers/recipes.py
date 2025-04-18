from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models.recipe import Recipe
from flask_app.models.user import User

@app.route('/recipes')
def dashboard():
    if 'user_id' not in session:
        return redirect('/')
    user = User.get_by_id({'id': session['user_id']})
    recipes = Recipe.get_all()
    return render_template('dashboard.html', user=user, recipes=recipes)

@app.route('/recipes/new')
def new_recipe():
    if 'user_id' not in session:
        return redirect('/')
    return render_template('new_recipe.html')

@app.route('/recipes/create', methods=['POST'])
def create_recipe():
    if not Recipe.validate(request.form):
        return redirect('/recipes/new')
    data = {
        **request.form,
        'user_id': session['user_id']
    }
    Recipe.save(data)
    return redirect('/recipes')

@app.route('/recipes/<int:id>')
def view_recipe(id):
    recipe = Recipe.get_by_id({'id': id})
    return render_template('view_recipe.html', recipe=recipe)

@app.route('/recipes/edit/<int:id>')
def edit_recipe(id):
    recipe = Recipe.get_by_id({'id': id})
    if recipe.user_id != session['user_id']:
        return redirect('/recipes')
    return render_template('edit_recipe.html', recipe=recipe)

@app.route('/recipes/update/<int:id>', methods=['POST'])
def update_recipe(id):
    if not Recipe.validate(request.form):
        return redirect(f'/recipes/edit/{id}')
    data = {**request.form, 'id': id}
    Recipe.update(data)
    return redirect('/recipes')

@app.route('/recipes/delete/<int:id>')
def delete_recipe(id):
    Recipe.delete({'id': id})
    return redirect('/recipes')
