from flask import render_template, send_from_directory

from server import app


@app.route('/')
def index():
    return send_from_directory('build','index.html')