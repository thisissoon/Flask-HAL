#!/usr/bin/env python
# encoding: utf-8

"""
flask_hal.document
==================

Module for constructing ``HAL`` documents.

Example:
    >>> from flask_hal.document import Document
    >>> d = Document()
    >>> d.to_dict()
"""

# Standard Libs
import json

# First Party Libs
from flask_hal import link


class BaseDocument(object):
    """Constructs a ``HAL`` document.
    """

    def __init__(self, data=None, links=None, embedded=None):
        """Base ``HAL`` Document. If no arguments are provided a minimal viable
        ``HAL`` Document is created.

        Keyword Args:
            data (dict): Data for the document
            links (flask_hal.link.Collection): A collection of ``HAL`` links
            embedded: TBC

        Raises:
            TypeError: If ``links`` is not a :class:`flask_hal.link.Collection`
        """

        self.data = data
        self.embedded = embedded or {}
        self.links = links or link.Collection()

    @property
    def links(self):
        return self._links

    @links.setter
    def links(self, value):
        if not isinstance(value, link.Collection):
            if isinstance(value, (list, set, tuple)):
                value = link.Collection(*value)
            else:
                raise TypeError('links must be a {0} or {1} instance'.format(
                                link.Collection, list))
        self._links = value

    @property
    def embedded(self):
        return self._embedded

    @embedded.setter
    def embedded(self, value):
        if not isinstance(value, dict):
            raise TypeError('embedded must be a {0} instance'.format(dict))
        self._embedded = value

    def to_dict(self):
        """Converts the ``Document`` instance into an appropriate data
        structure for HAL formatted documents.

        Returns:
            dict: The ``HAL`` document data structure
        """

        document = {}

        # Add Data to the Document
        if isinstance(self.data, dict):
            document.update(self.data)

        # Add Links
        if self.links:
            document.update(self.links.to_dict())

        # Add Embedded: Embedded API TBC
        if self.embedded:
            document.update({
                '_embedded': dict(
                    (n, v.to_dict()) for n, v in self.embedded.items()
                )
            })

        return document

    def to_json(self):
        """Converts :class:`.Document` to a ``JSON`` data structure.

        Returns:
            str: ``JSON`` document
        """

        return json.dumps(self.to_dict())


class Document(BaseDocument):
    """Constructs a ``HAL`` document.
    """

    def __init__(self, data=None, links=None, embedded=None):
        """Initialises a new ``HAL`` Document instance. If no arguments are
        provided a minimal viable ``HAL`` Document is created.

        Keyword Args:
            data (dict): Data for the document
            links (flask_hal.link.Collection): A collection of ``HAL`` links
            embedded: TBC

        Raises:
            TypeError: If ``links`` is not a :class:`flask_hal.link.Collection`
        """
        super(Document, self).__init__(data, links, embedded)
        self.links.append(link.Self())


class Embedded(BaseDocument):
    """Constructs a ``HAL`` embedded.

    Example:
        >>> document = Document(
        >>>     embedded={
        >>>         'orders': Embedded(
        >>>             embedded={'details': Embedded(
        >>>                 data={'details': {}}
        >>>             )},
        >>>             links=link.Collection(
        >>>                 link.Link('foo', 'www.foo.com'),
        >>>                 link.Link('boo', 'www.boo.com')
        >>>             ),
        >>>             data={'total': 30},
        >>>         )
        >>>     },
        >>>     data={'currentlyProcessing': 14}
        >>> )
        >>> document.to_json()
        ... {
                "_links": {
                    "self": {"href": "/entity/231"}
                },
                "_embedded": {
                    "orders": {
                        "_embedded": {
                            "details": {"details": {}}
                        },
                        "total": 30,
                        "_links": {
                            "foo": {"href": "www.foo.com"},
                            "boo": {"href": "www.boo.com"}
                        }
                    }
                },
                "currentlyProcessing": 14
            }
    """

    def to_dict(self):
        """Converts the ``Document`` instance into an appropriate data
        structure for HAL formatted documents.

        Returns:
            dict: The ``HAL`` document data structure
        """
        if isinstance(self.data, (list, tuple, set)):
            data = []

            for item in self.data:
                if isinstance(item, BaseDocument):
                    data.append(item.to_dict())
                else:
                    data.append(item)
            return data

        return super(Embedded, self).to_dict()
