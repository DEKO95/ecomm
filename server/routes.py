from deprecated import deprecated
from flask import render_template, send_from_directory

from server import app


@deprecated(reason="Will be removed after switching to the correct SPA model")
@app.route('/')
def index():
    return render_template('index.html')


@deprecated(reason="Will be removed after switching to the correct SPA model")
@app.route('/styles/styless.css')
def style():
    return send_from_directory('styles','styless.css')


@deprecated(reason="Will be removed after switching to the correct SPA model")
@app.route('/images/<img>')
def picture(img):
    return send_from_directory('images',img)
