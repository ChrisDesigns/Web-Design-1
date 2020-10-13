from bottle import get, template


@get('/route')
def index():
    return template("route")
