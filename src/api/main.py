# -*- coding: utf-8 -*-

from flask import Flask

application = Flask(__name__)
route = application.route
application.debug = True

@route('/')
def index():
	return "Hello World"

@route('/curtime')
def curtime():
	return '{"time": "2015-06-22 12:00"}'

def main():
	application.debug = True
	application.run()

if __name__ == "__main__":
	main()
