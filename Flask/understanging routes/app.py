
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello World!"

@app.route('/dojo')
def dojo():
    return "Dojo!"

@app.route('/say/<name>')
def say(name):
    return f"Hi {name}!"

@app.route('/repeat/<count>/<word>')
def repeat(count, word):
    return word * int(count)

if __name__ == "__main__":
    app.run(debug=True)
