from flask import render_template

from server_template import app


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')
