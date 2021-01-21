#!/usr/bin/python3
"""a script that starts a Flask web application"""

from flask import Flask
from flask import render_template
from models import storage
from models.state import State
app = Flask(__name__)


@app.route('/cities_by_states', strict_slashes=False)
def listStatesCities():
    """display a HTML page"""
    states = storage.all(State).values()
    return render_template("8-cities_by_states.html", states=states)


@app.teardown_appcontext
def teardown_db(self):
    """close 'em up"""
    storage.close()

if __name__ == '__main__':
        app.run(host='0.0.0.0', port=5000)
