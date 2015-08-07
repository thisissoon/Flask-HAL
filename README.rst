Flask-HAL
=========

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

Here is the resppnse from the above view.

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
