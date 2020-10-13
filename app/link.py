from bottle import get, template


@get('/link')
def link():
    return template("link")
