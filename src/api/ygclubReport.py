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
	sql = sql +"ORDER BY p.showtime DESC"
	res = execute_db_query(sql)
	print "res:"+str(len(res))
	#print res
	for item in res:
		print u'"'+str(item[3])+" "+item[4]+" "+item[8]+" "+timestamp_to_date(item[7])+'"'
def main():
	username = "squirrelRao"
	user = query_user_basic_info(username)
	if user == False:
		print "no user find by "+username
		return
	acts = get_ygclub_act_data(user["uid"])


main()
