import os
from app import home

# are we executing at PythonAnywhere?
ON_PYTHONANYWHERE = "PYTHONANYWHERE_DOMAIN" in os.environ
ON_PROD = ON_PYTHONANYWHERE and os.environ["PYTHONANYWHERE_DOMAIN"] == "webprod-chrisdesigns.pythonanywhere.com"

if ON_PYTHONANYWHERE:
    # on PA, set up to connect to the WSGI server
    from bottle import default_app
else:
    # on the development environment, import the development server
    from bottle import run

# set debug if not on prod (could be dev on PA)
if not ON_PROD:
    from bottle import debug
    debug(True)

if ON_PYTHONANYWHERE:
    # on PA, connect to the WSGI server
    application = default_app()
else:
    run(host='localhost', port=8080)
