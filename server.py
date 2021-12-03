from flask import Flask, render_template
app = Flask(__name__)

print(__name__)

@app.route('/')
def index():
    return render_template("index.html", height = 4, width = 4)

@app.route('/<int:num2>')
def height(num2):
    return render_template("index.html", width = 4, height = num2)

@app.route('/<int:num1>/<int:num2>')
def width_height(num1, num2):
    return render_template("index.html", width = int(num1 / 2), height = int(num2 / 2))

if __name__=="__main__":

    app.run(debug=True)