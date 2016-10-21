#!/usr/bin/env python
# encoding: utf-8

"""
Flask-HAL
---------

Provides easy integration of the  `HAL <https://tools.ietf.org/html/draft-kelly-json-hal-07>`_
specification for your ``REST`` Flask Applications.
"""

# Third Party Libs
from setuptools import setup


# Generate a Long Decription for the PyPi page which is the README.rst
# Plus the CHANGELOG.rst
long_description = open('./README.rst').read()
changelog = open('./CHANGELOG.rst').read()
long_description += '\n' + changelog

# Get Version
version = open('./VERSION.txt').read().strip()


setup(
    name='Flask-HAL',
    url='https://github.com/thisissoon/Flask-HAL',
    version=version,
    author='SOON_',
    author_email='dorks@thisissoon.com',
    description='Provides easy integration of the HAL specification for '
                'your REST Flask Applications.',
    long_description=long_description,
    packages=[
        'flask_hal',
    ],
    install_requires=[
        'flask',
    ],
    tests_require=[
        'pytest',
        'pytest_cov',
        'pytest_pep8',
        'pytest-flakes',
    ],
    setup_requires=[
        'pytest-runner',
    ],
    classifiers=[
        'Framework :: Flask',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Development Status :: 5 - Production/Stable',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Topic :: Software Development',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'License :: Public Domain'
    ],
    license='Public Domain',
    keywords=['Flask', 'HAL', 'REST', 'Views']
)
