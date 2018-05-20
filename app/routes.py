from flask import render_template, send_from_directory, request
from app import app
from app.utils import nocache
from app.config import config
from app import api


@app.route('/')
@app.route('/index')
@nocache
def index():
	user = {'username': 'Tal'}
	return render_template('index.html', title='Home', user=user, config=config)


@app.route('/start')
@nocache
def start():
	user = {'username': 'Tal'}
	return render_template('start.html', title='Start', user=user, config=config)


@app.route('/api/lcf', methods=['POST'])
@nocache
def lcf():
	print(request.get_json(force=True))
	return api.lcf(request.get_json(force=True))


@app.route('/static/<path:path>')
def send_js(path):
	return send_from_directory('static', path)