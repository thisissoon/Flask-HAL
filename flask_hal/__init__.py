#!/usr/bin/env python
# encoding: utf-8

"""
flask_hal
=========

Flask-HAL provides support for the ``HAL`` Specification within Flask allowing
you to build ``REST`` API responses which fulfil this specification.

Read more at the `Official Draft <https://tools.ietf.org/html/draft-kelly-json-hal-07>`_
"""


class HAL(object):
    """Enables Flask-HAL integration into Flask Applications, either by the
    Application Factory Pattern or directly into an already created Flask
    Application instance.

    This will set a custom ``response_class`` for the Application which
    handles the conversion of a ``HAL`` document response from a
    view into it's ``JSON`` representation.
    """

    def __init__(self, app=None, response_class=None):
        """Initialise Flask-HAL with a Flask Application. Acts as a proxy
        to :meth:`flask_hal.HAL.init_app`.

        Example:
            >>> from flask import Flask
            >>> from flask_hal import HAL
            >>> app = Flask(__name__)
            >>> HAL(app=app)

        Keyword Args:
            app (flask.app.Flask): Optional Flask application instance
            response_class (class): Optional custom ``response_class``
        """

        if app is not None:
            self.init_app(app, response_class=response_class)

    def init_app(self, app, response_class=None):
        """Initialise Flask-HAL with a Flask Application. This is designed to
        be used with the Flask Application Factory Pattern.

        Example:
            >>> from flask import Flask
            >>> from flask_hal import HAL
            >>> app = Flask(__name__)
            >>> HAL().init_app(app)

        Args:
            app (flask.app.Flask): Flask application instance

        Keyword Args:
            response_class (class): Optional custom ``response_class``
        """

        pass
