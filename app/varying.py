import datetime
from bottle import get, template, redirect, request, response


@get('/varying')
def varying():
    cookie_value = request.get_cookie("likes_jazz")
    cookie_with_default = cookie_value if cookie_value else "no"
    return template("varying", likes_jazz=cookie_with_default, current_time=datetime.datetime.now())


@get('/toggle')
def toggle():
    answer = request.get_cookie("likes_jazz")
    # find the opposite value of current answer
    opposite_state = "no" if answer == "yes" else "yes"
    # set that value if state exists, otherwise it's a yes
    new_state = opposite_state if answer else "yes"
    response.set_cookie("likes_jazz", new_state)
    redirect("/varying")