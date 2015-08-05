#!/usr/bin/env python
# encoding: utf-8

"""
flask_hal.link
==============

Implements the ``HAL`` Link specification.
"""


class Link(object):
    """
    """

    def __init__(
            self,
            href,
            name=None,
            title=None,
            link_type=None,
            deprecation=None,
            profile=None,
            templated=None,
            hreflang=None):
        """
        """

        self.href = href
        self.name = name
        self.title = title
        self.link_type = link_type,
        self.deprecation = deprecation
        self.profile = profile
        self.templated = templated
        self.hreflang = hreflang
