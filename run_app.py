#!/usr/bin/env python
# -*- coding: utf-8 -*-
from appium import webdriver
import time as t
def get_driver():
	desired_caps = {}
	desired_caps['platformName'] = "Android"  # 声明是ios还是Andriveroid系统
	# desired_caps['platformVersion'] = '6.0.1'  # mumuAndriveroid内核版本号，可以在夜神模拟器设置中查看
	desired_caps['platformVersion'] = '5.1.1'  # mumuAndriveroid内核版本号，可以在夜神模拟器设置中查看
	# desired_caps['deviceName'] = '127.0.0.1:7555'  # 连接的设备名称  mumu
	desired_caps['deviceName'] = '127.0.0.1:21503'  # 连接的设备名称 逍遥
	# desired_caps['app'] = 'C:\\Users\\TestSuit\Apptest\\imooc7.2.010102001andriveroid.apk'
	# desired_caps['unicodeKeyboard'] = True  # 输入法有中文的话 需要设置
	desired_caps['appPackage'] = 'cn.com.open.mooc'  # apk的包名
	desired_caps['appActivity'] = 'com.imooc.component.imoocmain.splash.MCSplashActivity'  # apk的launcherActivity
	# desired_caps['appWaitActivity'] = 'cn.com.open.mooc.index.splash.GuideActivity'  # Guiactivity真机运行报错
	# wait_activity()
	# desired_caps['unicodeKeyboard'] = 'True'  #unicode输入法
	# desired_caps['resetKeyboard'] = 'True'  #就是将键盘隐藏起来，可以sendkeys
	desired_caps['noReset'] = 'True'  # 启动app不清除app原有数据
	driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
	t.sleep(5)
	return driver

def get_size():
    #拿到屏幕的宽和高
	size = driver.get_window_size()
	witdth = size['width']
	height = size['height']
	return witdth,height

def swip_left():
	"""从右向左滑动 """
	# 从屏幕的右边  十分之九  处滑动
	x1 = get_size()[0]*0.9
	y1 = get_size()[1]*0.5
	#滑动到  屏幕的  十分之一处
	x = get_size()[0]*0.1
	driver.swipe(x1,y1,x,y1)

def swip_right():
	"""
	        从 左x 向 右x1 滑动 ，屏幕的十分之九  到十分之一
	        y=整个高的一般  中间
	        """
	x1 = get_size()[0] * 0.1
	y1 = get_size()[1] * 0.5
	x = get_size()[0] * 0.9
	driver.swipe(x1,y1,x,y1)

def swip_up():
    #向上滑动
	"""
	从底部想顶部滑动
	"""
	# 从屏幕底部中间位置  Y值有变化  从下向上  十分之九  滑到  十分之一
	x1 = get_size()[0] * 0.5
	y1 = get_size()[1] * 0.9
	y = get_size()[1] * 0.1
	driver.swipe(x1,y1,x,y1)

def swip_down():
	"""
			从屏幕的上部分 向下部分滑动
			从屏幕顶部的 十分之一  -----到下部的 十分之九
	"""
	x1 = get_size()[0] * 0.5
	y1 = get_size()[1] * 0.1
	y = get_size()[1] * 0.9
	driver.swipe(x1,y1,x1,y)

def swip_on(direction):
    if direction == 'up':
        swip_up()
    elif direction =='down':
        swip_down()
    elif direction =='left':
        swip_left()
    else:
        swip_right()

def go_login():
	"""点击到登录页面"""
	#登录进去点击账号”
	driver.find_element_by_xpath("//*[@text='账号']").click()
	# 点击去登陆
	driver.find_element_by_xpath("//*[@text='点击登录']").click()
	#跳转到注册页面 右上角的登录
	driver.find_element_by_id("cn.com.open.mooc:id/right_text").click()

def login():
	"""ID和 xpath 登录页面"""

	#清空账户框
	driver.find_element_by_id("cn.com.open.mooc:id/accountEdit").click()
	driver.find_element_by_id("cn.com.open.mooc:id/accountEdit").send_keys("18141923568")
	#清空密码框
	driver.find_element_by_id("cn.com.open.mooc:id/passwordEdit").clear()
	driver.find_element_by_id("cn.com.open.mooc:id/passwordEdit").send_keys("Cmcc@121122")
	#登录按钮
	driver.find_element_by_id("cn.com.open.mooc:id/loginLabel").click()

def login_by_class():
	#找到登录框的classname
	# print(element)
	#找到所有的classname为“android.widget.EditText”的地方 默认点击第一个
	elements = driver.find_elements_by_class_name("android.widget.EditText")
	# print(len(elements))   #一共有两个根据下标去取
	elements[0].send_keys("18141923568")
	# t.sleep(1)
	elements[1].send_keys("Cmcc@121122")
	#寻找登录按钮为  classname为“android.widget.RelativeLayout”的按钮  有五个  费劲
	elementsTwo = driver.find_elements_by_class_name("android.widget.RelativeLayout")
	# print(len(elementsTwo))
	# for i in elementsTwo:
	# 	i.click()
	#登录按钮就是第一个  索引为0
	elementsTwo[0].click()

def login_by_node():
	#先找到大的范围  在大的范围下再找下边的
	parelement = driver.find_element_by_id("cn.com.open.mooc:id/fl_content")
	#大的固定点找到了 ，再根据固定点去找
	elements = parelement.find_elements_by_class_name("android.widget.TextView")
	elements[0].send_keys("18141923568")
	elements[1].send_keys("CMcc@121122")

def login_by_uiautomater():
	driver.find_element_by_android_uiautomator('new UiSelector().text("手机号/邮箱")').clear()
	driver.find_element_by_android_uiautomator('new UiSelector().text("手机号/邮箱")').send_keys("18141923568")
	driver.find_element_by_android_uiautomator('new UiSelector().resourceId("cn.com.open.mooc:id/passwordEdit")').send_keys("18141923568")

driver = get_driver()
go_login()
login_by_uiautomater()
# login_by_class()
# login_by_class()
# login()












