# Third Party Libs
import flask
import pytest

# First Party Libs
from flask_hal import link
from flask_hal.document import Document, Embedded


def test_document_should_have_link_self():
    app = flask.Flask(__name__)
    with app.test_request_context('/entity/231'):
        document = Document()
        assert flask.request.path == document.links[0].href


def test_document_external_self():
    app = flask.Flask(__name__)
    with app.test_request_context('/entity/231'):
        document = Document(external_self=True)
        assert flask.request.url == document.links[0].href


def test_should_raise_exception_when_links_are_not_in_collection():
    app = flask.Flask(__name__)
    with app.test_request_context('/entity/231'):
        with pytest.raises(TypeError):
            Document(links=link.Link('foo', 'www.foo.com'))


def test_should_append_embedded_document():
    app = flask.Flask(__name__)
    with app.test_request_context('/entity/231'):
        document = Document(
            embedded={
                'orders': Embedded(
                    embedded={'details': Embedded(
                        data={'details': {}}
                    )},
                    links=link.Collection(
                        link.Link('foo', 'www.foo.com'),
                        link.Link('boo', 'www.boo.com')
                    ),
                    data={'total': 30},
                )
            },
            data={'currentlyProcessing': 14}
        )
        expected = {
            '_links': {
                'self': {
                    'href': flask.request.path
                }
            },
            '_embedded': {
                'orders': {
                    '_links': {
                        'foo': {'href': 'www.foo.com'},
                        'boo': {'href': 'www.boo.com'}
                    },
                    '_embedded': {
                        'details': {'details': {}}
                    },
                    'total': 30,
                }
            },
            'currentlyProcessing': 14
        }
        assert expected == document.to_dict()


def test_document_link_as_list_is_converted_to_collection():
    app = flask.Flask(__name__)
    with app.test_request_context('/entity/231'):
        document = Document(links=[link.Link('foo', 'www.foo.com')])
        assert isinstance(document.links, link.Collection)
        assert 2 == len(document.links)


def test_empty_document_to_json():
    app = flask.Flask(__name__)
    with app.test_request_context('/foo/23'):
        document = Document()
        expected = '{"_links": {"self": {"href": "/foo/23"}}}'
        assert expected == document.to_json()


def test_should_raise_exception_when_embedded_is_not_dict():
    app = flask.Flask(__name__)
    with app.test_request_context('/entity/231'):
        with pytest.raises(TypeError):
            Document(embedded=['details'])


def test_data_in_embedded_can_be_array():
    app = flask.Flask(__name__)
    with app.test_request_context('/entity/231'):
        document = Document(
            embedded={
                'order': Embedded(
                    data=[
                        {
                            'total': 30.00,
                            'currency': 'USD',
                            'status': 'shipped'
                        }, {
                            'total': 20.00,
                            'currency': 'USD',
                            'status': 'processing'
                        }
                    ]
                )
            },
            data={
                'currentlyProcessing': 14
            }
        )
        expected = {
            'currentlyProcessing': 14,
            '_links': {'self': {'href': u'/entity/231'}},
            '_embedded': {
                'order': [{
                    'total': 30.00,
                    'currency': 'USD',
                    'status': 'shipped'
                }, {
                    'total': 20.00,
                    'currency': 'USD',
                    'status': 'processing'
                }]
            }
        }
        assert expected == document.to_dict()


def test_data_in_embedded_can_be_array_of_documents():
    app = flask.Flask(__name__)
    with app.test_request_context('/entity/231'):
        document = Document(
            embedded={
                'order': Embedded(
                    data=[
                        Embedded(
                            data={
                                'total': 30.00,
                                'currency': 'USD',
                                'status': 'shipped'
                            },
                            links=link.Collection(
                                link.Link('foo', 'www.foo30.com'),
                                link.Link('boo', 'www.boo30.com')
                            ),
                        ),
                        Embedded(
                            data={
                                'total': 20.00,
                                'currency': 'USD',
                                'status': 'processing'
                            },
                            links=link.Collection(
                                link.Link('foo', 'www.foo20.com'),
                                link.Link('boo', 'www.boo20.com')
                            ),
                        )
                    ]
                )
            },
            data={
                'currentlyProcessing': 14
            }
        )
        expected = {
            'currentlyProcessing': 14,
            '_links': {'self': {'href': u'/entity/231'}},
            '_embedded': {
                'order': [
                    {
                        '_links': {
                            'foo': {'href': 'www.foo30.com'},
                            'boo': {'href': 'www.boo30.com'}
                        },
                        'total': 30.00,
                        'currency': 'USD',
                        'status': 'shipped'
                    },
                    {
                        '_links': {
                            'foo': {'href': 'www.foo20.com'},
                            'boo': {'href': 'www.boo20.com'}
                        },
                        'total': 20.00,
                        'currency': 'USD',
                        'status': 'processing'
                    }
                ]
            }
        }
        assert expected == document.to_dict()
