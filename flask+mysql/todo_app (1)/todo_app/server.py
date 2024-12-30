from flask import Flask, redirect, render_template, request, session
app = Flask(__name__)
app.secret_key = "Shhhhhh!!!!"
import uuid

# Display Routes
@app.route('/')
def home():
    if 'tasks' not in session:
        session['tasks'] = []
    id = uuid.uuid4()
    print(session)
    return render_template('home.html', tasks = session['tasks'], unique_id = id)

@app.route('/tasks/<id>')
def get_one(id):
    tasks = session['tasks']
    # task = {}
    # for t in tasks:
    #     if t['id'] == id:
    #         task=t
    task = [task for task in tasks if task['id'] == id][0]
    return render_template('on_task.html', task = task)
    


# Action Routes
@app.route('/add_task', methods=['post'])
def new_task():
    print("---BODY DATA: ", request.form)
    tasks = session['tasks']
    tasks.append(request.form)
    session['tasks'] = tasks
    return redirect('/')

@app.route('/tasks/<id>/delete')
def delete_task(id):
    updated_tasks = []
    for t in session['tasks']:
        if t['id'] != id:
            updated_tasks.append(t)
    session['tasks'] = updated_tasks
    return redirect('/')
    

if __name__=='__main__':
    app.run(debug=True)