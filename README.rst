Flask-HAL
=========

|circle| |downloads| |version| |license| |docs|

Hello Dave...

I provide easy integration of the  `HAL <https://tools.ietf.org/html/draft-kelly-json-hal-07>`_
specification for your ``REST`` Flask Applications.

Here is an example Dave...

.. sourcecode:: python

    # Third Party Libs
    from flask import Flask

    # First Party Libs
    from flask_hal import HAL, document


    app = Flask(__name__)
    HAL(app)  # Initialise HAL


    @app.route('/hello')
    def hello():
        return document.Document(data={
            'message': 'Hello World'
        })


    if __name__ == "__main__":
        app.run(debug=True)

Here is the response from the above view.

.. sourcecode:: http

    HTTP/1.1 200 OK
    Content-Type: application/hal+json; charset=UTF-8
    Date: Thu, 06 Aug 2015 10:24:04 GMT

    {
        "_links": {
            "self": {
                "href": "/hello"
            },
        },
        "foo": "bar"
    }

## Contributing

Run tests using `python setup.py test`.

.. |circle| image:: https://img.shields.io/circleci/project/thisissoon/Flask-HAL.svg
    :target: https://circleci.com/gh/thisissoon/Flask-HAL

.. |downloads| image:: http://img.shields.io/pypi/dm/Flask-HAL.svg
    :target: https://pypi.python.org/pypi/Flask-HAL

.. |version| image:: http://img.shields.io/pypi/v/Flask-HAL.svg
    :target: https://pypi.python.org/pypi/Flask-HAL

.. |license| image:: http://img.shields.io/pypi/l/Flask-HAL.svg
    :target: https://pypi.python.org/pypi/Flask-HAL

.. |docs| image:: https://img.shields.io/badge/documentation-latest-blue.svg
    :target: http://flask-hal.soon.build/en/latest/
