#!/usr/bin/env python
# encoding: utf-8

"""
flask_hal.link
==============

Implements the ``HAL`` Link specification.
"""

# Standard Libs
import json


VALID_LINK_ATTRS = [
    'name',
    'title',
    'type',
    'deprecation',
    'profile',
    'templated',
    'hreflang'
]


class Link(object):
    """Build ``HAL`` specification ``_links`` object.

    Example:
        >>> from flask_hal.link import Link
        >>> l = Link('foo', 'http://foo.com/bar')
        >>> print l.to_json()
        ... '{"foo": {"href": "http://foo.com/bar"}}'
        >>> l.title = 'Foo'
        >>> print l.to_json()
        ... '{"foo": {"href": "http://foo.com/bar", "name": "Foo"}}'

    """

    def __init__(self, rel, href, **kwargs):
        """Initialise a new ``Link`` object.

        Args:
            rel (str): The links ``rel`` or name
            href (str): The URI to the resource

        Keyword Args:
            name (str): The links name attribute, optional
            title (str): The links title attribute, optional
            type (str): The links type attribute, optional
            deprecation (str): The deprecation attribute, optional
            profile (str): The profile  attribute, optional
            templated (bool): The templated attribute, optional
            hreflang (str): The hreflang attribute, optional
        """

        self.rel = rel
        self.href = href

        for attr in VALID_LINK_ATTRS:
            if attr in kwargs:
                setattr(self, attr, kwargs.pop(attr))

    def to_json(self):
        """Returns the ``JSON`` encoded representation of the ``Link`` object.

        Returns:
            str: The ``JSON`` encoded object
        """

        # Minimum viable link
        link = {
            'href': self.href
        }

        # Add extra attributes if they exist
        for attr in VALID_LINK_ATTRS:
            if hasattr(self, attr):
                link[attr] = getattr(self, attr)

        return json.dumps({self.rel: link})
