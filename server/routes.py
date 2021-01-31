from flask import render_template, send_from_directory

from server import app


@app.route('/')
def index():
    return """<h1> Under construction </h1>"""