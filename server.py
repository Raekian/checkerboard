from flask import Flask, render_template
app = Flask(__name__)
import math


@app.route('/')
def index():
    x = 4
    y= 4
    return render_template('index.html', x = x, y = y)
    # return render_template('index.html')

@app.route('/<int:number>')
def onevalue(number):
    x = math.floor(int(number)/2)
    y = math.floor(int(number)/2)
    return render_template('index.html', x = x, y = y)

# @app.route('/play/<int:number>/<string:color>')
# def color(number, color):
#     x = number
#     y = color
#     return render_template('index.html', x = x, y = y)

if __name__ == "__main__":
    app.run(debug=True)