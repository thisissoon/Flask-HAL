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

# Third Party Libs
from flask_hal import link


class Document(object):
    """Constructs a ``HAL`` document.
    """

    def __init__(self, data=None, links=None, embedded=None):
        """Initialises a new ``HAL`` Document instance. If no arguments are
        proviced a minimal viable ``HAL`` Document is created.

        Keyword Args:
            data (dict): Data for the document
            links (flask_hal.link.Collection): A collection of ``HAL`` links
            embedded: TBC
        """

        self.data = data
        self.embedded = embedded  # TODO: Embedded API TBC

        # No links proviced, create an empty collection
        if links is None:
            links = link.Collection()

        # Always add the self link
        links.append(link.Self())

        self.links = links
