# -*- coding: utf-8 -*-

# Standard Libs
import datetime
import os
import sys


# Add flask_hal to the Path
root = os.path.abspath(
    os.path.join(
        os.path.dirname(__file__),
        '..',
    )
)

sys.path.append(os.path.join(root, 'flask_hal'))

# First Party Libs
import flask_hal  # noqa

# Project details
project = u'Flask-HAL'
copyright = u'{0}, SOON_ London Ltd'.format(datetime.datetime.utcnow().year)
version = '0.0.0'
release = version

# Sphinx Config
templates_path = ['_templates']
source_suffix = '.rst'
master_doc = 'index'

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.viewcode',
    'sphinx.ext.todo',
    'sphinx.ext.napoleon']

exclude_patterns = []

# Theme
sys.path.append(os.path.abspath('_themes'))
html_theme_path = ['_themes', ]
html_static_path = ['_static', ]
html_theme = 'kr'
html_sidebars = {
    'index':    ['sidebar_intro.html', 'localtoc.html', 'relations.html',
                 'sourcelink.html', 'searchbox.html'],
    '**':       ['sidebar_intro.html', 'localtoc.html', 'relations.html',
                 'sourcelink.html', 'searchbox.html']
}
