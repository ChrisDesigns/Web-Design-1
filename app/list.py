from bottle import get, template
from app.database import return_execute


@get("/list")
def list():
    result = return_execute("select * from todo")
    return template("list", rows=result)