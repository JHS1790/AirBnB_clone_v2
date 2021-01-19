#!/usr/bin/python3
"""a script that starts a Flask web application"""

from flask import Flask
from flask import render_template
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_world():
    """display “Hello HBNB!”"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """display “HBNB””"""
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def cisnotfun(text):
    """display “C ” followed by the value of the text variable”"""
    text = text.replace("_", " ")
    return 'C %s' % text


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def pythonisnotcool(text="is cool"):
    """display “Python ”, followed by the value of the text variable”"""
    text = text.replace("_", " ")
    return 'Python %s' % text


@app.route('/number/<int:n>', strict_slashes=False)
def nsucks(n):
    """display “n is a number” only if n is an integer”"""
    return '%d is a number' % n


@app.route('/number_template/<int:n>', strict_slashes=False)
def nsucksinhtml(n):
    """display “n is a number” only if n is an integer”"""
    return render_template('5-number.html', n=n)

if __name__ == '__main__':
        app.run(host='0.0.0.0', port=5000)
