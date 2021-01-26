from flask import render_template, redirect, url_for
from server import app

@app.errorhandler(404)
def not_found_error(error):
    # TODO
    # I think it should redirect user to something like ...com/404
    # but flask.redirect does not work properly 
    return render_template('404.html'), 404