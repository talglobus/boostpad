# import logging
# from logging.handlers import RotatingFileHandler
import sys
print(sys.version)

from flask import Flask

app = Flask(__name__)
# app.debug = True	# TODO: Find out why this isn't doing anything

from app import routes

# handler = RotatingFileHandler('boostedlogs.log', maxBytes=10000, backupCount=1)
# handler.setLevel(logging.INFO)
# app.logger.addHandler(handler)