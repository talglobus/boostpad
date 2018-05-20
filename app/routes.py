from flask import render_template
from app import app
from app.utils import nocache


@app.route('/')
@app.route('/index')
@nocache
def index():
	user = {'username': 'Tal'}
	return render_template('index.html', title='Home', user=user)