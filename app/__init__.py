from flask import Flask

app = Flask(__name__)
# app.debug = True	# TODO: Find out why this isn't doing anything

from app import routes