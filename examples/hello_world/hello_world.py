#!/usr/bin/env python
# encoding: utf-8

"""
A Simple Example Flask Application
==================================
"""

# Third Party Libs
from flask import Flask
from flask_hal import HAL, document


app = Flask(__name__)
HAL(app)  # Initialise HAL


@app.route('/hello')
def foo():
    return document.Document(data={
        'message': 'Hello World'
    })


if __name__ == "__main__":
    app.run()
