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
db.news.insert({"type":"阳光快报","content":"9月24日林科院新人培训信息在阳光地图可查询","link":"none","status":1})
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
db.school.insert({"name":"定福小学","address":"昌平区定福黄庄","contactor":"凡杰","phone":"15222757129","image":imageDomain+"/img/school/dingfu.jpg","location":"116.267228,40.106039","gather_location":"116.293844,40.094891","course":"计算机、绘本、英语、舞蹈、足球","class_weekday":"周日","class_time":"9:30","period":2,"priority":1})
db.school.insert({"name":"朱房村社区","address":"海淀区清河朱房村","contactor":"keyball","phone":"17701367266","image":imageDomain+"/img/school/zhufangcun.jpg","location":"116.330485,40.028045","gather_location":"116.320193,40.033007","course":"围棋","class_weekday":"周六","class_time":"14:30","period":2,"priority":1})
db.school.insert({"name":"费家村社区","address":"朝阳区崔各庄","contactor":"蕾蕾豆","phone":"13552687751","image":imageDomain+"/img/school/feijiacun.jpg","location":"116.505466,40.01589","gather_location":"116.493586,40.022727","course":"趣味主题课","class_weekday":"周六","class_time":"15:30","period":2,"priority":1})
db.school.insert({"name":"西店社区","address":"昌平区定福黄庄","contactor":"小塔","phone":"15810331634","image":imageDomain+"/img/school/xidian.jpg","location":"116.275796,40.110334","gather_location":"116.293844,40.094891","course":"魔法阅读","class_weekday":"周六","class_time":"9:30","period":2,"priority":1})
db.school.insert({"name":"新世纪图书馆","address":"海淀区上地","contactor":"刘新宇","phone":"18511801329","image":imageDomain+"/img/school/xinsiji.jpg","location":"116.328107,40.028392","gather_location":"116.320193,40.033007","course":"英语","class_weekday":"周六","class_time":"14:30","period":2,"priority":1})
db.school.insert({"name":"金盏社区","address":"朝阳区金盏乡","contactor":"歪果仁","phone":"15811285843","image":imageDomain+"/img/school/jinzhan.jpg","location":"116.568902,40.003503","gather_location":"116.568902,40.003503","course":"魔法数学","class_weekday":"周六","class_time":"14:00","period":2,"priority":2})
db.school.insert({"name":"新人培训林科院专场","address":"中国林业科学研究院","contactor":"凡杰","phone":"15222757129","image":imageDomain+"/img/school/dingfu.jpg","location":"116.248,40.00451","gather_location":"116.249962,40.00399","course":"新人培训","class_weekday":"9月24日周日","class_time":"14:30","period":3,"priority":0})

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
var time = 1508565600 + ( i -1 )* 24 * 3600 * 7  
db.class_schedule.insert({"name":"魔法数学","school":"金盏社区","semester":"2017年秋季学期","class_number":i,"class_time":time,"teacher":"","image":imageDomain+"/img/class_schedule/shuxue2.jpg"})
}

//init tigang
db.class_plan.remove({})
db.class_plan.insert({"semester":"2017年秋季学期","school":"定福小学","name":"绘本","class_number":1,"content":"<p>1宣布三项要求：1三次扰乱离开教室；2举手提问；3大声洪亮<br>2开始绘本：观察图片，列出提纲，集体朗读，分角色朗读<br>3中间穿插一个发散思维问题：六只火柴排出4个等边三角形。引导出三维空间的概念。<br>4复述课文。讲述类似的身边经历。<br>5看电影，鼹鼠的故事，伴你高飞，推荐小朋友自己观看，猜想视频的内容。<br>6环保小卫士，超能力，保护环境梦想绘画，下节课回顾可用。最深感想一句话。最佳表现学生，奖品。</p>"})
db.class_plan.insert({"semester":"2017年秋季学期","school":"定福小学","name":"足球","class_number":1,"content":"<p>第一节课<br>介绍足球课<br>介绍足球队的约定及保险相关事宜<br>热身准备活动<br>讲解带球-单脚直线<br>带球练习<br>讲解带球-单脚直线加转弯<br>带球练习 <br><br>第二节课<br>讲解停球<br>停球练习讲解传球（短传）<br>短传 + 停球 1对1练习<br>队内连续赛<br>课程总结"})
db.class_plan.insert({"semester":"2017年秋季学期","school":"费家村社区","name":"趣味主题","class_number":1,"content":"<p>课程为绘本故事、艺术创作、科学实验、财商养成<br>等多主题综合课程<br>教学目的是保持与激发孩子们的想象力，玩中学，学中乐<br></p>"})
db.class_plan.insert({"semester":"2017年秋季学期","school":"费家村社区","name":"趣味主题","class_number":2,"content":"《中秋小宴》<br>一、教学目标<br><br>1.了解中国传统文化之节日中秋及其情感内涵<br>2.温习中秋诗词<br>3.亲做月饼赠家人<br>4.体验中秋习俗<br><br>二、教学步骤<br><br>1.引入：关于中秋你能想到哪些词？<br>2.什么时间过中秋？<br>八月十五是农历，正说明了这是独属于我们华夏民族的传统节日。<br>3.每个节日都有传说<br>嫦娥奔月、玉兔捣药、吴刚伐桂（简略过一下）<br>3.中秋节是怎么来的？<br>秋收季节齐欢庆<br>周代时期祭月神<br>汉代江浙观大潮<br>魏晋时期始赏月<br>唐初才定节庆日<br>唐朝时期行拜月<br>文人雅士对诗会<br>北宋中秋始团圆<br>碧波江上放花灯<br>南宋始提“中秋节”<br>月夜百姓玩月忙<br>灯谜会上斗聪明<br>投壶射礼考眼力<br>明代始食团圆饼<br>螃蟹膏肥田螺鲜<br>福建博饼好彩头<br>明清流行送月饼<br>清代北京玩兔爷<br>桂花美酒最芬芳<br><br>4.根据以上总结中秋节要点（用第一节课《结构思考力》的知识）<br>（1）中秋节吃什么<br>月饼、水果、螃蟹、田螺、桂花酒<br>（2）中秋节做什么<br>拜月、走月（送月饼）、观潮、团圆、放灯、对诗<br>（3）中秋节玩什么<br>猜灯谜、投壶、博饼、玩兔爷<br>5.诗歌结对子（小游戏）<br>每个同学会拿到纸条（年纪小的孩子与助教一组），上面是两句有关中秋或月亮的诗（选他们学过的）。由其中一位同学念出来，手里拿着和他的诗合为一首的同学要马上向他靠拢，所有同学结对完毕后检验对错，并请大家来解释诗歌大意。<br>5.做月饼<br>带孩子们一起动手做桃山皮月饼（因诗结对的同学互相帮助）<br>（1）讲述传统月饼做法<br>（2）示范制作过程<br>（3）每个同学可以制作4粒月饼打包装带回家送给爸爸妈妈，还有一张卡片请大家写一些祝福语。<br>6.玩游戏（游戏时间根据实际情况安排）<br>（1）猜灯谜游戏<br>准备一些简单有趣的灯谜让大家猜，猜对最多的小组同学有奖励。<br>（2）投壶游戏<br>准备投壶道具，每人每轮有三次机会投掷，投掷最多的小组有奖励。<br><br>大家可以在十一假期和自己的家人朋友一起玩。让中秋节不只是吃月饼这么简单。<br><br>三、总结<br><br>希望我们珍惜我们的传统节日，更珍惜我们和家人在一起的快乐时光，提前祝大家中秋快乐！<br>"})
db.class_plan.insert({"semester":"2017年秋季学期","school":"定福小学","name":"绘本","class_number":2,"content":"主题关键词： 分享&改变<br><br>课堂目标<br>1、了解绘本内容，能够用自己的语言讲述这个故事。<br>2、发挥自己的想象力，续写绘本。对于低年级的同学，应该能够用绘画、剪贴等方式，加上简单的文字，表达清楚自己的想法；对于高年级的同学，能够用完整的段落续写故事。鼓励每个人至少想出两种不同的结局。<br><br>一、预热（10分钟）<br>（声明纪律：想说话先举手，别人回答问题时认真倾听，自己回答问题时声音洪亮）<br>回忆上节课的绘本，引出这节课的主题。<br>l  上节课大家读了什么绘本？一起来回忆一下吧。<br>l  我们这次讲的绘本是一个叫乔恩·克拉森的人写的。他写了三本关于帽子的绘本，以后有机会老师都会讲给大家听。<br>l  这节课，我想和大家一起分享的绘本故事叫做《我们发现了一顶帽子》。大家看封面，“我们”是谁啊？两只乌龟有什么不同呢？我们一起来给它们起个名字吧。<br>l  大家觉得这两只乌龟发现这顶帽子之后，会发生什么样的事情呢？<br><br>二、绘本阅读（30分钟）<br>带领孩子们一起阅读绘本，引发大家的思考。<br>（第一遍老师引导，大家一起朗读。第二遍老师带领大家回顾绘本，回顾时要做到：1、分清哪些话是A乌龟说的，哪些话是B乌龟说的；2、一起为空白页补上合适的话。第三遍翻看时，老师和同学一起讨论下面的问题；）<br><br>l  大家觉得这两只乌龟是什么关系？<br>l  两只乌龟住在哪里？<br>l  你觉得这两只乌龟带上帽子好看吗？它们自己能看到自己带帽子的样子吗？如果有人说它带上帽子不好看，它还会带这顶帽子吗？<br>l  “我们一个有帽子，另一个没有，这就不对了”，为什么会这么说？<br>l  乌龟为什么要一起看日落？<br>l  A乌龟是真的“什么也没想”吗？<br>l  B乌龟是真的睡着了吗？<br>l  第二天醒来，会发生什么事情呢？<br><br>课间休息（20分钟）<br><br>三  绘本续写（40分钟）<br><br>1、导入<br>这个绘本故事现在有三章，我们还可以自己继续写下去。第三章停在了两只乌龟做的梦里。上节课老师最后问了大家一个问题——第二天醒来，又会发生什么样的事情呢？<br>老师先讲一个自己的想法。我也很希望听到大家创造的绘本故事。<br><br>2、创作绘本第四章<br>发给同学彩笔，白纸。请同学们用各种方法创作自己的绘本第四章。低年级的同学可以用绘画、剪贴的方式，高年级同学主要用文字的方式。助教老师也要参与。<br><br>3. 分享故事<br>台上准备一顶帽子。谁想好了就可以来到台上，带上帽子，讲自己的故事。<br>要求：<br>1、声音洪亮，全班同学都能听清；<br>2、不能和前面的人重复。<br>3、故事不能少于5句话。<br>4、故事完整。<br>所有上台的同学得到一张明信片做奖励。明信片随机抽取。助教老师要在合适的时候参与。<br><br>4 制作绘本<br>没有得到上台机会的同学，或者太害羞不愿意上台讲的同学，可以课下把自己的故事写完整，然后这节课或者下节课交给老师。老师会帮你把它做成属于你自己的绘本。<br><br>要求：<br>图或文字完整清楚。老师可以帮你配上图或者修改文字，但如果两样都不清楚，老师就没有办法了……<br><br>课堂准备<br>彩笔10-12盒，A4白纸50张."})
db.class_plan.insert({"semester":"2017年秋季学期","school":"定福小学","name":"足球","class_number":2,"content":""})
//db.class_plan.insert({"semester":"2017年秋季学期","school":"定福小学","name":"足球","class_number":1,"content":""})
