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


class Links(object):
    """Build a collection of ``HAL`` link objects.

    Example:
        >>> from flask_hal.link import Link, Links
        >>> l = Links(
        ...     Link('foo', 'http://foo.com'),
        ...     Link('bar', 'http://bar.com'))
        >>> print l.to_json()
        ... {
        ...     "_links": {
        ...         "foo": {
        ...             "href": "http://foo.com"
        ...         },
        ...         "bar": {
        ...             "href": "http://bar.com"
        ...         }
        ...     }
        ... }
    """

    def __init__(self, *args):
        """Initialise a new ``Links`` object.

        Example:
            >>> l = Links(
            ...     Link('foo', 'http://foo.com'),
            ...     Link('bar', 'http://bar.com'))

        Raises:
            TypeError: If a link is not a ``flask_hal.link.Link`` instance
        """

        self.links = []
        self.index = 0

        for link in args:
            if not isinstance(link, Link):
                raise TypeError(
                    '{0} is not a valid flask_hal.link.Link instance'.format(link))

            self.links.append(link)

    def __getitem__(self, index):
        """Get a specific link by index.
        """

        return self.links[index]

    def __iter__(self):
        """Makes the ``Links`` object iterable.
        """

        return self

    def __len__(self):
        """Returns the number of links.
        """

        return len(self.links)

    def __next__(self):
        """Iterate to the next item.

        Returns:
            Link: The next link object

        Raises:
            StopIteration
        """

        try:
            link = self.links[self.index]
        except IndexError:
            raise StopIteration
        self.index += 1

        return link

    def next(self):
        """Support for Python 2.x iterators.
        """

        return self.__next__()

    def append(self, link):
        """Appends a ``Link`` object to the ``Links``.

        Args:
            link (flask_hal.link.Link): The ``Link`` object to add

        Raises:
            TypeError: If the ``link`` argument is not a ``flask_hal.link.Link``
        """

        if not isinstance(link, Link):
            raise TypeError(
                '{0} is not a valid flask_hal.link.Link instance'.format(link))

        self.links.append(link)

    def to_dict(self):
        """Returns the Python ``dict`` representation of the ``Links`` instance.

        Example:
            >>> from flask_hal.link import Link, Links
            >>> l = Links(
            ...     Link('foo', 'http://foo.com'),
            ...     Link('bar', 'http://bar.com'))
            >>> l.to_dict()
            ... {'_links': {'bar': {'href': 'http://bar.com'},
            ... 'foo': {'href': 'http://foo.com'}}}

        Returns:
            dict
        """

        links = {}

        for link in self.links:
            links.update(link.to_dict())

        return {
            '_links': links
        }

    def to_json(self):
        """Returns the ``JSON`` representation of the instance.

        Example:
            >>> from flask_hal.link import Link, Links
            >>> l = Links(
            ...     Link('foo', 'http://foo.com'),
            ...     Link('bar', 'http://bar.com'))
            >>> l.to_json()
            ... '{"_links": {"foo": {"href": "http://foo.com"}, "bar": {"href": "http://bar.com"}}}'

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
