from flask import render_template, send_from_directory
from app import app
from app.utils import nocache
from app.config import config


@app.route('/')
@app.route('/index')
@nocache
def index():
	user = {'username': 'Tal'}
	return render_template('index.html', title='Home', user=user)


@app.route('/start')
@nocache
def start():
	user = {'username': 'Tal'}
	return render_template('start.html', title='Start', user=user, config=config)

@app.route('/static/<path:path>')
def send_js(path):
	return send_from_directory('static', path)