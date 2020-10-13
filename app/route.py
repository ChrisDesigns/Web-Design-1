from bottle import get, template


@get('/route')
def route():
    return template("route")
