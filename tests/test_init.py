#!/usr/bin/env python
# encoding: utf-8

"""
tests.test_init
===============

Tests for the init module.
"""

# Standard Libs
import json

# Third Party Libs
from flask import Flask, Response

# First Party Libs
from flask_hal import HAL, HALResponse, document


class TestHAL(object):

    def test_init(self):
        app = Flask(__name__)
        HAL(app)

        assert app.response_class == HALResponse

    def test_can_set_custom_response_class(self):
        app = Flask(__name__)
        HAL(app, Response)

        assert app.response_class == Response


class TestHalResponse(object):

    def test_returns_document_with_hal_document(self):
        app = Flask(__name__)
        with app.test_request_context():
            d = document.Document()
            r = HALResponse.force_type(d, {})

        expected = json.dumps({
            '_links': {
                'self': {
                    'href': '/'
                }
            }
        })

        assert isinstance(r, Response)
        assert r.headers['Content-Type'] == 'application/hal+json'
        assert r.data.decode("utf-8") == expected

    def test_returns_standard_response(self):
        r = HALResponse.force_type(Response('foo'), {})

        assert isinstance(r, Response)
        assert r.headers['Content-Type'] == 'text/html; charset=utf-8'
        assert r.data.decode("utf-8") == 'foo'
