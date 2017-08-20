# -*- coding: utf-8 -*-
import logging
import os
import sys
import time
from flask import Flask
from flask import request
from logging.handlers import TimedRotatingFileHandler
from util import api
from caiyun.platform.redis_client import client as rc
from caiyun.platform.mongo_client import client as mongo_client

application = Flask(__name__)
route = application.route
application.debug = True
logger = application.logger

@route('/v1/')
def index():
	return "Hello LEAD`"

@route('/v1/curtime')
@api
def curtime():
	return {"time": "2015-06-22 12:00"}


@route('/v1/banner')
@api
def get_banner():
	logger.debug("query banner infos")
	db = mongo_client.lead
	banner = db.banner
        banners = []
	result = {"banner":banners}
	response = {"status":"ok","result":result}
	dbresults = banner.find();
	for x in dbresults:
		item = {"image":x["image"],"link":x["link"]}
		banners.append(item)
        return response		


@route('/v1/news')
@api
def get_news():
	logger.debug("query lead news")
	db = mongo_client.lead
	news = db.news
	news_items = []
	result = {"news":news_items}
	response = {"status":"ok","result":result}
	dbresults = news.find({"status":1})
	for x in dbresults:
		item = {"content":x["content"],"link":x["link"]}
		news_items.append(item)
	return response
	

@route('/v1/school')
@api
def get_school():
	logger.debug("query lead schools")
	db = mongo_client.lead
	school = db.school
	school_items = []
	result = {"school":school_items}
	response = {"status":"ok","result":result}
	dbresults = school.find()
	for x in dbresults:
		item = {"name":x["name"]}
		school_items.append(item)
	return response

@route('/v1/course')
@api
def get_course():
	logger.debug("query lead courses")
	db = mongo_client.lead
	course = db.course
	course_items = []
	result = {"course":course_items}
	response = {"status":"ok","result":result}
	dbresults = course.find()
	for x in dbresults:
		item = {"name":x["name"]}
		course_items.append(item)
	return response

@route('/v1/<string:lonlat>/leadmap')
@api
def leadmap(lonlat):
	logger.debug("leadmap api")
	db = mongo_client.lead
	school = db.school
	map_items = []
	result = {"school":map_items}
	response = {"status":"ok","result":result}
	dbres = school.find()
	for x in dbres:
		item = {"name":x["name"],"address":x["address"],"image":x["image"],"distance":-1,"location":x["location"],"gather_location":x["gather_location"],"course":x["course"],"class_weekday":x["class_weekday"],"class_time":x["class_time"],"period":x["period"]}
		map_items.append(item)
	return response
	
def main():
	application.debug = True
	application.run()

if __name__ == "__main__":
	main()
