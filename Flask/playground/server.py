from flask import Flask, render_template

app = Flask(__name__)

# Default route: 3 blue boxes
@app.route('/play')
def play_default():
    return render_template("play.html", num_boxes=3, color="blue")

# Route for 'x' boxes
@app.route('/play/<int:x>')
def play_x(x):
    return render_template("play.html", num_boxes=x, color="blue")

# Route for 'x' boxes with a specific color
@app.route('/play/<int:x>/<color>')
def play_x_color(x, color):
    return render_template("play.html", num_boxes=x, color=color)

if __name__ == "__main__":
    app.run(debug=True)
