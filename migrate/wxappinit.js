var conn=new Mongo('127.0.0.1:27017')
var db=conn.getDB('lead')
var imageDomain = "https://squirrelrao.com"
//init index page banners
db.banner.remove({})
db.banner.insert({"name":"课程表","image":imageDomain+"/img/banner/kechengbiao.jpg","link":"../../pages/schedule/schedule","seq":3})
db.banner.insert({"name":"欢迎使用","image":imageDomain+"/img/banner/welcome_use.jpg","link":"home","seq":1})
db.banner.insert({"name":"项目地图","image":imageDomain+"/img/banner/newclass.jpg","link":"../../pages/coordinate/coordinate","seq":2})


//init lead news
db.news.remove({})
db.news.insert({"type":"阳光快报","content":"2017年秋季学期将于9月16日正式开学","link":"none","status":1})
// db.news.insert({"type":"阳光快报","content":"阳光小程序正式上线：）","link":"none","status":1})


//init course
db.course.remove({})
db.course.insert({"name":"魔法数学"})
db.course.insert({"name":"英语"})
db.course.insert({"name":"计算机"})
db.course.insert({"name":"足球"})
db.course.insert({"name":"围棋"})
db.course.insert({"name":"绘本"})
db.course.insert({"name":"舞蹈"})
db.course.insert({"name":"魔法阅读"})
db.course.insert({"name":"趣味主题"})

//init project
db.school.remove({})
db.school.insert({"name":"定福小学","address":"昌平区定福黄庄","contactor":"凡杰","phone":"15222757129","image":imageDomain+"/img/school/dingfu.jpg","location":"116.267228,40.106039","gather_location":"116.293844,40.094891","course":"计算机、绘本、英语、舞蹈、足球","class_weekday":"周日","class_time":"9:30","period":2})
db.school.insert({"name":"朱房村社区","address":"海淀区清河朱房村","contactor":"keyball","phone":"17701367266","image":imageDomain+"/img/school/zhufangcun.jpg","location":"116.330485,40.028045","gather_location":"116.320193,40.033007","course":"围棋","class_weekday":"周六","class_time":"14:30","period":2})
db.school.insert({"name":"费家村社区","address":"朝阳区崔各庄","contactor":"蕾蕾豆","phone":"13552687751","image":imageDomain+"/img/school/feijiacun.jpg","location":"116.505466,40.01589","gather_location":"116.493586,40.022727","course":"趣味主题课","class_weekday":"周六","class_time":"15:30","period":2})
db.school.insert({"name":"西店社区","address":"昌平区定福黄庄","contactor":"小塔","phone":"15810331634","image":imageDomain+"/img/school/xidian.jpg","location":"116.275796,40.110334","gather_location":"116.293844,40.094891","course":"魔法阅读","class_weekday":"周六","class_time":"9:30","period":2})
db.school.insert({"name":"新世纪图书馆","address":"海淀区上地","contactor":"刘新宇","phone":"18511801329","image":imageDomain+"/img/school/xinsiji.jpg","location":"116.328107,40.028392","gather_location":"116.320193,40.033007","course":"英语","class_weekday":"周六","class_time":"14:30","period":2})
db.school.insert({"name":"金盏社区","address":"朝阳区金盏乡","contactor":"歪果仁","phone":"15811285843","image":imageDomain+"/img/school/jinzhan.jpg","location":"116.568902,40.003503","gather_location":"116.568902,40.003503","course":"魔法数学","class_weekday":"周六","class_time":"14:00","period":2})



//init class schedule
db.class_schedule.remove({})
//定福小学
for(i = 1;i <= 10; i++){
var time = 1505611800 + ( i -1 )* 24 * 3600 * 7  
db.class_schedule.insert({"name":"英语","school":"定福小学","semester":"2017年秋季学期","class_number":i,"class_time":time,"teacher":"","image":imageDomain+"/img/class_schedule/yingyu2.jpg"})
db.class_schedule.insert({"name":"舞蹈","school":"定福小学","semester":"2017年秋季学期","class_number":i,"class_time":time,"teacher":"","image":imageDomain+"/img/class_schedule/wudao2.jpg"})
db.class_schedule.insert({"name":"计算机","school":"定福小学","semester":"2017年秋季学期","class_number":i,"class_time":time,"teacher":"","image":imageDomain+"/img/class_schedule/jisuanji2.jpg"})
db.class_schedule.insert({"name":"足球","school":"定福小学","semester":"2017年秋季学期","class_number":i,"class_time":time,"teacher":"","image":imageDomain+"/img/class_schedule/zuqiu2.jpg"})
db.class_schedule.insert({"name":"绘本","school":"定福小学","semester":"2017年秋季学期","class_number":i,"class_time":time,"teacher":"","image":imageDomain+"/img/class_schedule/yuwenke2.jpg"})
}

//西店
for(i = 1;i <= 10; i++){
var time = 1508549400 + ( i -1 )* 24 * 3600 * 7  
db.class_schedule.insert({"name":"魔法阅读","school":"西店社区","semester":"2017年秋季学期","class_number":i,"class_time":time,"teacher":"","image":imageDomain+"/img/class_schedule/yuwenke2.jpg"})
}

//朱房村
for(i = 1;i <= 10; i++){
var time = 1508565600 + ( i -1 )* 24 * 3600 * 7  
db.class_schedule.insert({"name":"围棋","school":"朱房村社区","semester":"2017年秋季学期","class_number":i,"class_time":time,"teacher":"","image":imageDomain+"/img/class_schedule/weiqi2.jpg"})
}



//新世纪
for(i = 1;i <= 10; i++){
var time = 1507962600 + ( i -1 )* 24 * 3600 * 7  
db.class_schedule.insert({"name":"英语","school":"新世纪图书馆","semester":"2017年秋季学期","class_number":i,"class_time":time,"teacher":"","image":imageDomain+"/img/class_schedule/yingyu2.jpg"})
}

//费家村
for(i = 1;i <= 10; i++){
var time = 1505547000 + ( i -1 )* 24 * 3600 * 7  
db.class_schedule.insert({"name":"趣味主题","school":"费家村社区","semester":"2017年秋季学期","class_number":i,"class_time":time,"teacher":"","image":imageDomain+"/img/class_schedule/xingqu2.jpg"})
}


//金盏
for(i = 1;i <= 10; i++){
var time = 1506146400 + ( i -1 )* 24 * 3600 * 7  
db.class_schedule.insert({"name":"魔法数学","school":"金盏社区","semester":"2017年秋季学期","class_number":i,"class_time":time,"teacher":"","image":imageDomain+"/img/class_schedule/shuxue2.jpg"})
}

//init tigang
db.class_plan.remove({})
db.class_plan.insert({"semester":"2017年秋季学期","school":"定福小学","name":"绘本","class_number":1,"content":"<p>1宣布三项要求：1三次扰乱离开教室；2举手提问；3大声洪亮<br>2开始绘本：观察图片，列出提纲，集体朗读，分角色朗读<br>3中间穿插一个发散思维问题：六只火柴排出4个等边三角形。引导出三维空间的概念。<br>4复述课文。讲述类似的身边经历。<br>5看电影，鼹鼠的故事，伴你高飞，推荐小朋友自己观看，猜想视频的内容。<br>6环保小卫士，超能力，保护环境梦想绘画，下节课回顾可用。最深感想一句话。最佳表现学生，奖品。</p>"})
db.class_plan.insert({"semester":"2017年秋季学期","school":"定福小学","name":"足球","class_number":1,"content":"<p>第一节课<br>介绍足球课<br>介绍足球队的约定及保险相关事宜<br>热身准备活动<br>讲解带球-单脚直线<br>带球练习<br>讲解带球-单脚直线加转弯<br>带球练习 <br><br>第二节课<br>讲解停球<br>停球练习讲解传球（短传）<br>短传 + 停球 1对1练习<br>队内连续赛<br>课程总结"})
db.class_plan.insert({"semester":"2017年秋季学期","school":"费家村社区","name":"趣味主题","class_number":1,"content":"<p>课程为绘本故事、艺术创作、科学实验、财商养成<br>等多主题综合课程<br>教学目的是保持与激发孩子们的想象力，玩中学，学中乐<br></p>"})
