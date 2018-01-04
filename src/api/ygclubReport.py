# -*- coding: utf-8 -*-  
import MySQLdb
import time

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
	print db
	print sql
	res = []
	cursor = db.cursor()
	try:
		cursor.execute(sql)
		results = cursor.fetchall()
		for row in results:
			res.append(row)
		print "sql query res len:"+str(len(res))
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
	user = {"username":username,"uid":res[0][0],"email":res[0][1],"regdate":timestamp_to_date(res[0][12]),"avatar":avatar}
	return user


#get ygclub activity statistics
def get_ygclub_act_data(uid):
	sql = "SELECT pe.uid, pe.username, pe.config, pe.checkin, p.class, p.tid, p.ctid, p.showtime, t.subject  FROM "
	sql = sql +"bbs_ygclub_partyers as pe LEFT JOIN bbs_ygclub_party as p on pe.tid = p.tid "
	sql = sql +"LEFT JOIN bbs_forum_thread as t on p.tid = t.tid where 1 "
	sql = sql +"AND pe.uid = '"+str(uid)+"' "
	sql = sql +"AND pe.verified = 4 "
	sql = sql +"AND t.subject NOT LIKE '%活动取消%' "
	sql = sql +"ORDER BY p.showtime ASC"
	res = execute_db_query(sql)
	print "res:"+str(len(res))
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
	for item in res:
		print u'"'+str(item[3])+" "+item[4]+" "+item[8]+" "+timestamp_to_date(item[7])+'"'
		#get first school activity
		if u'【活动召集】' in u''+item[8]+'' and u'阳光公益活动' in u''+item[4]+'' and school_name == "":
			school_name = get_school_name(item[8])
			school_date = timestamp_to_date(item[7])
		yghd_count = yghd_count  + 1
		if u''+item[4]+'' == u'阳光公益活动':
			ygkt_count = ygkt_count + 1
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
	count_data = {"ygkt_count":ygkt_count,"yglh_count":yglh_count,"ygpx_count":ygpx_count,"ygxx_count":ygxx_count,"ygwb_count":ygwb_count,"yghd_count":yghd_count,"kids_count":kids_count,"teach_plan_count":teach_plan_count}
	print count_data
	time_data = {"ygkt_hour":ygkt_hour_count,"yghd_starttime":yghd_starttime,"yghd_endtime":yghd_endtime}
	print time_data
	first_activity = {"school_name":school_name,"date":school_date}
	print first_activity
	return first_activity


def get_school_name(data):
	projects = ["","","","","","","","","","","","","","","","",""]
	project = "-"
	return project

def main():
	username = "squirrelRao"
	user = query_user_basic_info(username)
	if user == False:
		print "no user find by "+username
		return
	acts = get_ygclub_act_data(user["uid"])


main()