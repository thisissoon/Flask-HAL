#!/usr/bin/env python
# encoding: utf-8

"""
tests.test_link
===============

Unittests for the :module:`flask_hal.link` module.
"""

# Standard Libs
import json

# First Party Libs
from flask_hal.link import Link


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
