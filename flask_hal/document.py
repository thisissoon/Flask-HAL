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


class Document(object):
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

        self.data = data
        self.embedded = embedded  # TODO: Embedded API TBC

        # No links provided, create an empty collection
        if links is None:
            links = link.Collection()
        else:
            if not isinstance(links, link.Collection):
                raise TypeError('links must be a flask_hal.link.Collection instance')

        # Always add the self link
        links.append(link.Self())

        self.links = links

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
        document.update(self.links.to_dict())

        # Add Embedded TODO: Embedded API TBC
        document.update(self.embedded)

        return document

    def to_json(self):
        """Converts :class:`.Document` to a ``JSON`` data structure.

        Returns:
            str: ``JSON`` document
        """

        return json.dumps(self.to_dict())
