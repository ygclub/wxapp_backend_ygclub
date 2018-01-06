# -*- coding: utf-8 -*- 
import sys 
reload(sys) 
sys.setdefaultencoding('utf8') 
import MySQLdb
import time
import json
import random

SCHOOLS=['费家村','金盏社区','定福学校','新世纪图书馆','爱加倍','东坝中心','成长驿站','西店','水厂大院','怀柔育才','朱房村','经纬学校','燕京小天鹅','汇蕾学校','桃园学校','崔各庄','新公民学校','育英学校','宜民学校','文德学校','弘立学校','育才学校','农民之子图书馆','振华学校','光明学校','信心学校','木兰社区','毛菊图书馆','蓝天丰苑学校']

#timestamp to time
def timestamp_to_date(timestamp):
	timeArray = time.localtime(timestamp)
	return time.strftime("%Y-%m-%d", timeArray)

#open mysql db connection
def open_connect():
	db = MySQLdb.connect("127.0.0.1","lead","MagGN_i.))7","www_ygclub_org",charset="utf8")
	return db

#close db conection
def close_connect(db):
	db.close()


#query db
def execute_db_query(sql):
	db = open_connect()
	#print db
	#print sql
	res = []
	cursor = db.cursor()
	try:
		cursor.execute(sql)
		results = cursor.fetchall()
		for row in results:
			res.append(row)
		#print "sql query res len:"+str(len(res))
	except e:
		print "error:"+e
	close_connect(db)
	return res

#query user id
def query_user_basic_info(username):
	sql = "select * from bbs_common_member where username ='"+username+"'"
	res = execute_db_query(sql)
	if len(res) < 1:
		return False
	user = {}
	avatar = "http://www.ygclub.org/uc/avatar.php?uid="+str(res[0][0])+"&size=middle"
	user = {"username":username,"uid":res[0][0],"email":res[0][1],"regdate":timestamp_to_date(res[0][12]),"regdate_timestamp":res[0][12],"avatar":avatar}
	return user


#query tong qi sheng
def get_tongqisheng(date,username):
	min_date = date - 2678400 #30天范围
	max_date = date + 2678400
	sql = "select username from bbs_common_member where username != '"+username+"' and regdate >= "+str(min_date)+" and regdate <= "+str(max_date)
	res = execute_db_query(sql)
	max_count = 8
	tongqisheng = []
	if len(res) <= max_count:
		return res
	i = 0
	while i < max_count:
		position = random.randint(0,len(res)-1)
		tongqisheng.append(res[position][0])
		i = i + 1
		res.remove(res[position])
	return tongqisheng

#get ygclub activity statistics
def get_ygclub_act_data(user):
	#print user["username"]+"的阳光公益报告"
	uid = user["uid"]
	sql = "SELECT pe.uid, pe.username, pe.config, pe.checkin, p.class, p.tid, p.ctid, p.showtime, t.subject, pe.usertask  FROM "
	sql = sql +"bbs_ygclub_partyers as pe LEFT JOIN bbs_ygclub_party as p on pe.tid = p.tid "
	sql = sql +"LEFT JOIN bbs_forum_thread as t on p.tid = t.tid where 1 "
	sql = sql +"AND pe.uid = '"+str(uid)+"' "
	sql = sql +"AND pe.verified = 4 "
	sql = sql +"AND t.subject NOT LIKE '%活动取消%' "
	sql = sql +"ORDER BY p.showtime ASC"
	res = execute_db_query(sql)
	#print "res:"+str(len(res))
	#print res
	data = {}
	ygkt_count = 0 #阳光课堂活动次数
	yglh_count = 0 #阳光例会次数
	ygpx_count = 0 #阳光培训次数
	ygxx_count = 0 #阳光休闲活动次数
	ygwb_count = 0 #其它外部活动次数
	yghd_count = 0 #阳光活动总数
	school_name = "" #第一次活动项目点
	school_date = "" #第一次活动时间
	px_date = "" #第一次培训时间
	service_schools = []
	zhujiang_count = 0
	first_zhujiang_date = ""
	first_zhujiang_school = ""
	for item in res:
		#print u'"'+str(item[3])+" "+item[4]+" "+item[8]+" "+timestamp_to_date(item[7])+'"'
		#get first school activity
		if u'主讲' in u''+item[9]+'':
			if first_zhujiang_date == "":
				first_zhujiang_date = timestamp_to_date(item[7])
				first_zhujiang_school = u''+get_school_name(item[8])+''
			zhujiang_count = zhujiang_count + 1
		if u'【活动召集】' in u''+item[8]+'' and u'阳光公益活动' in u''+item[4]+'' and school_name == "":
			school_name = u''+get_school_name(item[8])+''
			school_date = timestamp_to_date(item[7])
			service_schools.append(school_name)
		if (u'培训活动召集' in u''+item[8]+'' and u'阳光公益活动' in u''+item[4]+'') or (u'活动召集' in u''+item[4]+'' and u'培训交流' in u''+item[4]+''):
			px_date = timestamp_to_date(item[7])
		yghd_count = yghd_count  + 1
		if u''+item[4]+'' == u'阳光公益活动':
			ygkt_count = ygkt_count + 1
			service_school_name = u''+get_school_name(item[8])+''
			if service_school_name not in service_schools and service_school_name != "":
				service_schools.append(service_school_name)
		elif u''+item[4]  == u'阳光例会':
			yglh_count = yglh_count + 1
		elif u''+item[4]+'' == u'培训交流':
			ygpx_count = ygpx_count + 1
		elif u''+item[4]+'' == u'休闲活动' or u''+item[4]+'' == u'交流活动':
			ygxx_count = ygxx_count + 1
		elif u''+item[4]+'' == u'外部公益活动' :
			ygwb_count = ygwb_count + 1
	ygkt_hour_count = ygkt_count * 2
	yghd_starttime = timestamp_to_date(res[0][7])
	yghd_endtime = timestamp_to_date(res[len(res)-1][7])
	kids_count = ygkt_count * 12
	teach_plan_count = ygkt_count/2
	jiaoan_count = zhujiang_count
	infos = {}
	count_data = {"ygkt_count":ygkt_count,"yglh_count":yglh_count,"ygpx_count":ygpx_count,"ygxx_count":ygxx_count,"ygwb_count":ygwb_count,"yghd_count":yghd_count,"kids_count":kids_count,"teach_plan_count":teach_plan_count}
	#print count_data
	time_data = {"ygkt_hour":ygkt_hour_count,"yghd_starttime":yghd_starttime,"yghd_endtime":yghd_endtime}
	#print time_data
	first_activity = {"school_name":school_name,"school_date":school_date,"train_date":px_date}
	#print json.dumps(first_activity, encoding="UTF-8", ensure_ascii=False)
	serice_school_info = {"school_count":len(service_schools),"school_list":service_schools}
	#print json.dumps(serice_school_info, encoding="UTF-8", ensure_ascii=False)
	zhujiang_info = {"first_zhujiang_date":first_zhujiang_date,"first_zhujiang_school":first_zhujiang_school,"zhujiang_count":zhujiang_count,"jiaoan_count":jiaoan_count}
	#print json.dumps(zhujiang_info, encoding="UTF-8", ensure_ascii=False)
	tongqisheng = get_tongqisheng(user['regdate_timestamp'],user['username'])
	#tongqisheng_info = {"tongqisheng":tongqisheng}
	#print json.dumps(tongqisheng_info, encoding="UTF-8", ensure_ascii=False)
	infos = {"count":count_data,"time":time_data,"school":serice_school_info,"first_info":first_activity,"zhujiang_info":zhujiang_info,"tongqisheng":tongqisheng}
	return infos


def get_school_name(data):
	project = ""
	for item in SCHOOLS:
		if u''+item+'' in data:
			project = item
	return project

def get_report(username):
	user = query_user_basic_info(username)
	if user == False:
		print "no user find by "+username
		return
	info = get_ygclub_act_data(user)
	data = {"user":user,"detail":info}
	#print json.dumps(data, encoding="UTF-8", ensure_ascii=False)
	return data
#get_report("squirrelRao")
