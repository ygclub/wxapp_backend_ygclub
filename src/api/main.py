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
	dbresults = banner.find().sort("seq",1);
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
		item = {"type":x["type"],"content":x["content"],"link":x["link"]}
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
                timeHour = int(x["class_time"].split(":")[0])+2
                classEnd_time = str(timeHour)+":"+x["class_time"].split(":")[1]
		item = {"name":x["name"],"address":x["address"],"contactor":x["contactor"],"phone":x["phone"],"image":x["image"],"distance":-1,"location":x["location"],"gather_location":x["gather_location"],"course":x["course"],"class_weekday":x["class_weekday"],"class_time":x["class_time"]+"-"+classEnd_time,"period":x["period"]}
		map_items.append(item)
	return response

@route('/v1/query_class_schedule',methods=['POST'])
@api
def query_class_schedule():
	logger.debug("get class schedule")
	req_form = request.form
	school_param = req_form["school"]
	course_param = req_form["course"]
	keyword = req_form["keyword"]
	sort = req_form["sort"]
		
	db = mongo_client.lead
	class_schedule = db.class_schedule
	items = []
	result = {"schedule":items}
	response = {"status":"ok","result":result}
        if sort == "1":
		 dbres = class_schedule.find().sort([("name",1),("class_time",1)])
        elif sort == "2":
		dbres = class_schedule.find().sort([("school",1),("class_time",1)])
	elif sort == "3":
		dbres = class_schedule.find().sort("class_time",1)
	else:
		dbres = class_schedule.find().sort([("class_time",1),("school",1),("name",1)])
	for x in dbres:
		if school_param != "all" and x["school"] != school_param:
			continue
		if course_param != "all" and x["name"] != course_param:
			continue
		if keyword != "none":
			if keyword in x["name"] or keyword in x["school"] or keyword in x["semester"]:
				time_local = time.localtime(x["class_time"])
				endTime_local = time.localtime(x["class_time"]+3600*2)
				class_date = time.strftime("%Y-%m-%d",time_local)
				class_time = time.strftime("%H:%M",time_local)
				classEnd_time = time.strftime("%H:%M",endTime_local)
				item = {"school":x["school"],"course":x["name"],"image":x["image"],"teacher":x["teacher"],"semester":x["semester"],"class_number":x["class_number"],"teacher":x["teacher"],"date":class_date,"timerange":class_time+"-"+classEnd_time,"period":2}
				items.append(item)
		else:
			time_local = time.localtime(x["class_time"])
			endTime_local = time.localtime(x["class_time"]+3600*2)
			class_date = time.strftime("%Y-%m-%d",time_local)
			class_time = time.strftime("%H:%M",time_local)
			classEnd_time = time.strftime("%H:%M",endTime_local)
			item = {"school":x["school"],"course":x["name"],"image":x["image"],"teacher":x["teacher"],"semester":x["semester"],"class_number":x["class_number"],"teacher":x["teacher"],"date":class_date,"timerange":class_time+"-"+classEnd_time,"period":2}
			items.append(item)
	return response


@route('/v1/query_class_detail',methods=['POST'])
@api
def query_class_detail():
	logger.debug("query class detail")
	req_form = request.form
        school = req_form["school"]
        class_name = req_form["class_name"]
        class_number = req_form["class_number"]
        semester = req_form["semester"]
        db = mongo_client.lead
        class_schedule = db.class_schedule
        schedule = {}
        plan = {"content":""}
        result = {"class":schedule,"plan":plan}
        response = {"status":"ok","result":result}
        logger.debug(school+" - " + class_name + " - " +class_number + " - " + semester)
        dbres = class_schedule.find({"school":school,"semester":semester,"name":class_name,"class_number":int(class_number)})
        for x in dbres:
                logger.debug("find:"+x["name"])
		time_local = time.localtime(x["class_time"])
		endTime_local = time.localtime(x["class_time"]+3600*2)
		class_date = time.strftime("%Y-%m-%d",time_local)
		class_time = time.strftime("%H:%M",time_local)
		classEnd_time = time.strftime("%H:%M",endTime_local)
                schedule["school"] = x["school"]
                schedule["course"] = x["name"]
                schedule["image"] = x["image"]
                schedule["teacher"] = x["teacher"]
                schedule["semester"] = x["semester"]
                schedule["class_number"] = x["class_number"]
                schedule["date"] = class_date
                schedule["timerange"] = class_time+"-"+classEnd_time
                schedule["period"] = 2
	class_plan = db.class_plan 
        dbres = class_plan.find({"school":school,"semester":semester,"name":class_name,"class_number":int(class_number)})
        for y in dbres:
	 	 plan["content"] = y["content"]
        return response


@route('/v1/regist',methods=['POST'])
@api
def regist():
	logger.debug("regist")
        req_form = request.form
        uid = req_form["uid"]
        nickname = req_form["nickname"]

        db = mongo_client.lead
        user = db.user
        user.update({"nickname":nickname},{"$set":{"uid":uid,"nickname":nickname,"time":time.time()}},upsert=True)
	return {"status":"ok"}
				
def main():
	application.debug = True
	application.run()

if __name__ == "__main__":
	main()
