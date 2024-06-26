#!/usr/bin/env python3
"""
Setting up a basic flask app
"""
from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def index():
    """
    Returns the template if index.html
    """
    return render_template('0-index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
