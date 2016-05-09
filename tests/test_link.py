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
import pytest
from flask import Flask

# First Party Libs
from flask_hal.link import Collection, Link, Self


class TestCollection(object):

    def test_init_raises_type_error(self):
        with pytest.raises(TypeError) as excinfo:
            Collection(
                Link('foo', '/foo'),
                'Foo',
                Link('bar', '/bar'))

        assert 'Foo is not a valid flask_hal.link.Link instance' in str(excinfo.value)

    def test_to_dict(self):
        c = Collection(
            Link('foo', '/foo'),
            Link('bar', '/bar'))

        expected = {
            '_links': {
                'foo': {
                    'href': '/foo'
                },
                'bar': {
                    'href': '/bar'
                }
            }
        }

        assert c.to_dict() == expected

    def test_to_dict_repeat_relation(self):
        c = Collection(
            Link('foo', '/foo'),
            Link('foo', '/bar'))

        expected = {
            '_links': {
                'foo': [
                    {
                        'href': '/foo'
                    },
                    {
                        'href': '/bar'
                    }
                ]
            }
        }

        assert c.to_dict() == expected

    def test_to_json(self):
        c = Collection(
            Link('foo', '/foo'),
            Link('bar', '/bar'))

        expected = json.dumps({
            '_links': {
                'foo': {
                    'href': '/foo'
                },
                'bar': {
                    'href': '/bar'
                }
            }
        })

        assert c.to_json() == expected

    def test_to_json_repeat_relation(self):
        c = Collection(
            Link('foo', '/foo'),
            Link('foo', '/bar'))

        expected = json.dumps({
            '_links': {
                'foo': [
                    {
                        'href': '/foo'
                    },
                    {
                        'href': '/bar'
                    }
                ]
            }
        })

        assert c.to_json() == expected


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
                    'href': '/',
                    'name': 'foo',
                }
            }

            assert l.to_dict() == expected

    def test_to_json(self):
        with self.app.test_request_context():
            l = Self(foo='foo', name='foo')

            expected = json.dumps({
                'self': {
                    'href': '/',
                    'name': 'foo',
                }
            })

            assert l.to_json() == expected

    def test_with_server_name(self):
        self.app.config['SERVER_NAME'] = 'foo.com'
        with self.app.test_request_context():
            l = Self(foo='foo', name='foo')

            expected = {
                'self': {
                    'href': 'http://foo.com/',
                    'name': 'foo',
                }
            }

            assert l.to_dict() == expected
