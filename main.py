from flask import Flask, render_template, send_from_directory
app = Flask(__name__)

@app.route('/')
def main_page():
    return render_template('example.html')

@app.route('/styles/styless.css')
def style():
    return send_from_directory('styles','styless.css')

@app.route('/images/pel.jpg')
def picture():
    return send_from_directory('images','pel.jpg')

if __name__ == '__main__':
    app.run(
      host='0.0.0.0',
      port=2000
      )
