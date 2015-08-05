# Flask-HAL
Flask Extension to easily add support for REST HATEOAS via the HAL Specification:
https://tools.ietf.org/html/draft-kelly-json-hal-07

## With Kim (ideas)

``` python
@app.route('/foo/:id')
def foo_view(id):
    foo = Foo.query.get(id)
    data = FooSerializer().serialize(foo)

    document = Document(links=Links(foo.hal_link()), data=data)

    return document, 200
```
