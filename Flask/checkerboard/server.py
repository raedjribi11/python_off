from flask import Flask, render_template  
app = Flask(__name__) 

@app.route('/')
def checkerboard_default():
    return render_template("checkerboard.html", rows=8, cols=8)

@app.route('/<int:cols>')
def checkerboard_rows(cols):
    return render_template("checkerboard.html", rows=8, cols=cols)

@app.route('/<int:rows>/<int:cols>')
def checkerboard_custom(rows, cols):
    return render_template("checkerboard.html", rows=rows, cols=cols)


if __name__ == "__main__":
    app.run(debug=True)
