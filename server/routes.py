from flask import render_template, send_from_directory

from server import app


@app.route('/')
def index():
    return render_template('public/index.html')