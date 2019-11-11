from flask import *
from datetime import datetime
import Calculator as calculator
app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    data = "Deploying a Flask App To Heroku"
    return render_template('index.html')

@app.route('/add')
def add():
    a = num(request.args.get('a'))
    b = num(request.args.get('b'))
    return str(calculator.add(a,b))

@app.route('/minus')
def minus():
    a = num(request.args.get('a'))
    b = num(request.args.get('b'))
    return str(calculator.minus(a,b))

@app.route('/times')
def times():
    a = num(request.args.get('a'))
    b = num(request.args.get('b'))
    return str(calculator.times(a,b))

@app.route('/divided')
def divided():
    a = num(request.args.get('a'))
    b = num(request.args.get('b'))
    return str(calculator.divided(a,b))


def num(s):
    try:
        return int(s)
    except ValueError:
        return float(s)

if __name__ == '__main__':
    app.run(debug=True)
