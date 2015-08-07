# Third Party Libs
import flask
import pytest

# First Party Libs
from flask_hal.document import Document, Embedded
from flask_hal import link


def test_document_should_have_link_self():
    app = flask.Flask(__name__)
    with app.test_request_context('/entity/231'):
        document = Document()
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
                    'href': flask.request.url
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
        expected = '{"_links": {"self": {"href": "http://localhost/foo/23"}}}'
        assert expected == document.to_json()


def test_should_raise_exception_when_embedded_is_not_dict():
    app = flask.Flask(__name__)
    with app.test_request_context('/entity/231'):
        with pytest.raises(TypeError):
            Document(embedded=['details'])
