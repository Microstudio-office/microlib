#版权声明：任何人均不可复制该文档内容！
def qp()
  	from os import system as xt
    xt("clear")

def f_p(nr,sj):
        print("该功能暂时停用")
def open(web):
	import webbrowser
	webbrowser.open(web)


def 薪酬万能计算():
	from time import sleep as 暂停一下
	from os import system as 系统
	def 薪酬计算(工时,工价):
	    if 工时 >= 24:
	        时间=工时-24
	        print( '''
	        你是真的皮，都说时间是公平的，你就比别人多活点{}个小时/天是吧。
	        '''.format(时间))
	    elif 工时 <=0:
	        return print('''
	        三和大神，日结一天。阔以玩三天。{}小时/天这样的工种都被你做了。
	        '''.format(工时))
	    elif 工价 <=0 :
	        return '''
	        富二代是不用干活的，还算什么薪酬。吃吃喝喝又一天了，对吧。
	        '''
	 
	    月薪=工价*工时*23
	 
	    if 月薪 <= 50:
	        return '''
	        月薪{}元/月。天天上网，电费都亏完了。
	        '''.format(月薪)
	 
	    elif (月薪 > 50) and (月薪 < 5000):
	        return '''
	        很好，月薪{}元/月刚好拖了我国平均工资后腿。
	        '''.format(月薪)
	 
	    elif (月薪 >= 5000) and (月薪 <= 6000):
	        return '''
	        嘿嘿，月薪{}元/月刚好到平均收入。
	        '''.format(月薪)
	 
	    elif (月薪 > 6000) and (月薪 <= 10000):
	        return '''
	        白领就是白领，月薪{}元/月都是高人一等的。
	        '''.format(月薪)
	 
	    elif 月薪 > 10000:
	        return '''
	        月薪{}元/月。土豪，还缺朋友吗？
	        '''.format(月薪)
	 
	 
	print('欢迎使用薪酬万能计算工具，本工具使用最前沿的算法。结合21世纪大数据，22世纪人工智能等多种高新技术研发而成，计算后的结果，绝对让你大吃自己一惊。\n由微机工作室提供技术支持')
	 
	while True:
	    print('输入你每天的工作时间，请填数字，单位（小时/天）：',end='')
	    工时=input()
	    try:
	        工时=int(工时)
	        break
	    except:
	        print('输入错误，请输入正确的数字！')
	        暂停一下(3)
	        系统('cls')
	        continue
	 
	while True:
	    print('输入你每小时的工价，请填数字，单位（元/小时）：',end='')
	    工价=input()
	    try:
	        工价=int(工价)
	        break
	    except:
	        print('输入错误，请输入正确的数字！')
	        暂停一下(3)
	        系统('cls')
	        continue
	 
	print('正在调用国家计算中心天河壹号为您计算薪酬，请稍等！')
	结果=薪酬计算(工时,工价)
	 
	计数=1
	for i in [5,4,3,2,1]:
	    暂停一下(计数)
	    print(i)
	    计数 += 1
	 
	系统('cls')
	 
	for i in range(5):
	    print('...')
	 
	print(结果)
	 
	for i in range(5):
	    print('...')


def logo():
	print("     \033[41m  \033[0m\033[42m  \033[0m\n     \033[44m  \033[0m\033[43m  \033[0m")
	print("微 机 工 作 室             \n")


def logo_picture():
	print("     \033[41m  \033[0m\033[42m  \033[0m\n     \033[44m  \033[0m\033[43m  \033[0m")

def logo_txt():
	print("微 机 工 作 室             \n")

def end():
	from tkinter import messagebox
	messagebox.showwarning("","大家看完以后可以给一个小心心吗？❤  谢谢大家！！！")


def ai_robot():
	import urllib.request
	import re
	import time
	while True:    
	    x = input("你：")    
	    x = urllib.parse.quote(x)  
	    time.sleep(1)
	    link = urllib.request.urlopen(        
	        "http://nlp.xiaoi.com/robot/webrobot?&callback=__webrobot_processMsg&data=%7B%22sessionId%22%3A%22ff725c236e5245a3ac825b2dd88a7501%22%2C%22robotId%22%3A%22webbot%22%2C%22userId%22%3A%227cd29df3450745fbbdcf1a462e6c58e6%22%2C%22body%22%3A%7B%22content%22%3A%22" + x + "%22%7D%2C%22type%22%3A%22txt%22%7D")    
	    html_doc = link.read().decode()    
	    reply_list = re.findall(r'\"content\":\"(.+?)\\r\\n\"', html_doc)    
	    print("小I：" + reply_list[-1])
	    time.sleep(1)
