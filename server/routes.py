from server import app

from flask import render_template, send_from_directory

@app.route('/')
def main_page():
    return render_template('index.html')

@app.route('/developers')
def developers():
    return render_template('developers.html')
    
@app.route('/styles/styless.css')
def style():
    return send_from_directory('styles','styless.css')

@app.route('/images/pel.jpg')
def picture():
    return send_from_directory('images','pel.jpg')