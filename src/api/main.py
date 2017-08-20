# -*- coding: utf-8 -*-

from flask import Flask
from flask import request
from logging.handlers import TimedRotatingFileHandler
from util import api
from caiyun.platform.redis_client import client as rc
from caiyun.platform.mongo_client import client as mongo_client
application = Flask(__name__)
route = application.route
application.debug = True

@route('/v1/')
def index():
	return "Hello LEAD`"

@route('/v1/curtime')
@api
def curtime():
	return {"time": "2015-06-22 12:00"}

def main():
	application.debug = True
	application.run()

if __name__ == "__main__":
	main()
