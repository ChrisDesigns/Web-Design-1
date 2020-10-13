from bottle import get, template


@get('/link')
def index():
    return template("link")
