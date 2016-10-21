#!/usr/bin/env python
# encoding: utf-8

"""
flask_hal.link
==============

Implements the ``HAL`` Link specification.
"""

# Standard Libs
import json

# Third Party Libs
from flask import current_app, request


VALID_LINK_ATTRS = [
    'name',
    'title',
    'type',
    'deprecation',
    'profile',
    'templated',
    'hreflang'
]


class Collection(list):
    """Build a collection of ``HAL`` link objects.

    Example:
        >>> from flask_hal.link import Collection, Link
        >>> l = Collection(
        ...     Link('foo', 'http://foo.com'),
        ...     Link('bar', 'http://bar.com'))
        >>> print l.to_dict()
        ... {
        ...     '_links': {
        ...         'foo': {
        ...             'href": "http://foo.com'
        ...         },
        ...         'bar': {
        ...             'href': 'http://bar.com'
        ...         }
        ...     }
        ... }
    """

    def __init__(self, *args):
        """Initialise a new ``Collection`` object.

        Example:
            >>> l = Collection(
            ...     Link('foo', 'http://foo.com'),
            ...     Link('bar', 'http://bar.com'))

        Raises:
            TypeError: If a link is not a ``flask_hal.link.Link`` instance
        """

        for link in args:
            if not isinstance(link, Link):
                raise TypeError(
                    '{0} is not a valid flask_hal.link.Link instance'.format(link))

            self.append(link)

    def to_dict(self):
        """Returns the Python ``dict`` representation of the ``Collection``
        instance.

        Example:
            >>> from flask_hal.link import Collection, Link
            >>> l = Collection(
            ...     Link('foo', 'http://foo.com'),
            ...     Link('bar', 'http://bar.com'))
            >>> l.to_dict()
            ... {'_links': {'bar': {'href': 'http://bar.com'},
            ... 'foo': {'href': 'http://foo.com'}}}

        Returns:
            dict
        """

        links = {}

        for link in self:
            if link.rel in links.keys():
                if isinstance(links[link.rel], dict):
                    links[link.rel] = [links[link.rel]]
                links[link.rel].append(link.to_dict()[link.rel])
            else:
                links.update(link.to_dict())

        return {
            '_links': links
        }

    def to_json(self):
        """Returns the ``JSON`` representation of the instance.

        Example:
            >>> from flask_hal.link import Collection, Link
            >>> l = Collection(
            ...     Link('foo', 'http://foo.com'),
            ...     Link('bar', 'http://bar.com'))
            >>> l.to_json()
            ... '{"_links":
                    {
                        "foo": {"href": "http://foo.com"},
                        "bar": {"href": "http://bar.com"}
                    }
                }'

        Returns:
            str: The ``JSON`` representation of the instance
        """

        return json.dumps(self.to_dict())


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

    def to_dict(self):
        """Returns the Python ``dict`` representation of the ``Link`` instance.

        Example:
            >>> from flask_hal.link import Link
            >>> l = Link('foo', 'http://foo.com')
            >>> l.to_dict()
            ... {'foo': {'href': 'http://foo.com'}}

        Returns:
            dict
        """

        # Minimum viable link
        link = {
            'href': self.href
        }

        # Add extra attributes if they exist
        for attr in VALID_LINK_ATTRS:
            if hasattr(self, attr):
                link[attr] = getattr(self, attr)

        return {
            self.rel: link
        }

    def to_json(self):
        """Returns the ``JSON`` encoded representation of the ``Link`` object.

        Example:
            >>> from flask_hal.link import Link
            >>> l = Link('foo', 'http://foo.com', name='Foo')
            >>> print l.to_json()
            ... '{"foo": {"href": "http://foo.com", "name": "Foo"}}'

        Returns:
            str: The ``JSON`` encoded object
        """
        return json.dumps(self.to_dict())


class Self(Link):
    """A class to create the required ``self`` link  from the current
    request URL.
    """

    def __init__(self, **kwargs):
        """Initialises a new ``Self`` link instance. Accepts the same
        Keyword Arguments as :class:`.Link`.

        See Also:
            :class:`.Link`
        """

        url = request.url
        if current_app.config['SERVER_NAME'] is None:
            url = request.url.replace(request.host_url, '/')

        return super(Self, self).__init__('self', url, **kwargs)
