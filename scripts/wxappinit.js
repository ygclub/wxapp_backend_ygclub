var conn=new Mongo('127.0.0.1:27017')
var db=conn.getDB('lead')
var imageDomain = "https://squirrelrao.com"
//init index page banners
db.banner.remove({})
db.banner.insert({"name":"课程表","image":imageDomain+"/img/banner/kechengbiao.jpg","link":"../../pages/schedule/schedule","seq":3})
db.banner.insert({"name":"欢迎使用","image":imageDomain+"/img/banner/welcome.jpg","link":"home","seq":1})
db.banner.insert({"name":"项目地图","image":imageDomain+"/img/banner/newclass.jpg","link":"../../pages/coordinate/coordinate","seq":2})


//init lead news
db.news.remove({})
db.news.insert({"type":"重要通知","content":"2017年秋季学期将于9月16日正式开学","link":"none","status":1})
db.news.insert({"type":"阳光快报","content":"阳光小程序正式上线：）","link":"none","status":1})


//init course
db.course.remove({})
db.course.insert({"name":"语文"})
db.course.insert({"name":"数学"})
db.course.insert({"name":"英语"})
db.course.insert({"name":"科普"})
db.course.insert({"name":"计算机"})
db.course.insert({"name":"足球"})
db.course.insert({"name":"围棋"})
db.course.insert({"name":"趣味经济"})
db.course.insert({"name":"绘本"})
db.course.insert({"name":"国学"})
db.course.insert({"name":"表演"})

//init project
db.school.remove({})
db.school.insert({"name":"定福小学","address":"昌平区定福黄庄","contactor":"凡杰","phone":"15222757129","image":imageDomain+"/img/school/dingfu.jpg","location":"116.267228,40.106039","gather_location":"116.293844,40.094891","course":"计算机、绘本、英语、舞蹈、足球","class_weekday":"周日","class_time":"9:30","period":2})
db.school.insert({"name":"朱房村社区","address":"海淀区清河朱房村","contactor":"keyball","phone":"17701367266","image":imageDomain+"/img/school/dingfu.jpg","location":"116.330485,40.028045","gather_location":"116.320193,40.033007","course":"趣味经济、围棋","class_weekday":"周六","class_time":"14:30","period":2})

//init class schedule
db.class_schedule.remove({})
for(i = 1;i <= 10; i++){
var time = 1505525400 + ( i -1 )* 24 * 3600 * 7  
db.class_schedule.insert({"name":"语文","school":"定福小学","semester":"2017年秋季学期","class_number":i,"class_time":time,"teacher":"三足乌","image":imageDomain+"/img/class_schedule/yuwen.jpg"})
}
//db.dict.remove({})
//db.dict.insert({code:"0",name:"未知的性别"})
//db.dict.insert({code:"1",name:"男"})
//db.dict.insert({code:"2",name:"女"})
