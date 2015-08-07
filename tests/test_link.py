#!/usr/bin/env python
# encoding: utf-8

"""
tests.test_link
===============

Unittests for the :module:`flask_hal.link` module.
"""

# Standard Libs
import json

# Third Party Libs
from flask import Flask

# First Party Libs
from flask_hal.link import Link, Self


class TestLink(object):

    def test_only_valid_link_attrs_set(self):
        l = Link('foo', '/foo', foo='foo', name='foo')

        assert not hasattr(l, 'foo')
        assert l.name == 'foo'

    def test_to_dict(self):
        l = Link('foo', '/foo', foo='foo', name='foo')

        expected = {
            'foo': {
                'href': '/foo',
                'name': 'foo',
            }
        }

        assert l.to_dict() == expected

    def test_to_json(self):
        l = Link('foo', '/foo', foo='foo', name='foo')

        expected = json.dumps({
            'foo': {
                'href': '/foo',
                'name': 'foo',
            }
        })

        assert l.to_json() == expected


class TestSelf(object):

    def setup(self):
        self.app = Flask(__name__)

    def test_only_valid_link_attrs_set(self):
        with self.app.test_request_context():
            l = Self(foo='foo', name='foo')

            assert not hasattr(l, 'foo')
            assert l.name == 'foo'

    def test_to_dict(self):
        with self.app.test_request_context():
            l = Self(foo='foo', name='foo')

            expected = {
                'self': {
                    'href': 'http://localhost/',
                    'name': 'foo',
                }
            }

            assert l.to_dict() == expected

    def test_to_json(self):
        with self.app.test_request_context():
            l = Self(foo='foo', name='foo')

            expected = json.dumps({
                'self': {
                    'href': 'http://localhost/',
                    'name': 'foo',
                }
            })

            assert l.to_json() == expected
