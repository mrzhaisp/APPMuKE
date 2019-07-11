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
	# desired_caps['unicodeKeyboard'] = 'True'  #unicode输入法
	# desired_caps['resetKeyboard'] = 'True'  #就是将键盘隐藏起来，可以sendkeys
	desired_caps['noReset'] = 'False'  # 启动app不清除app原有数据
	driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
	t.sleep(10)
	return driver

def get_size():
    #拿到屏幕的宽和高
	size = driver.get_window_size()
	witdth = size['width']
	height = size['height']
	return witdth,height

def swip_left():
    #向左滑动
	x1  = get_size()[0]/10*9
	y1 =  get_size()[1]/2
	x = get_size()[0]/10
	driver.swipe(x1,y1,x,y1)

def swip_right():
	#向右滑动
	x1  = get_size()[0]/10
	y1 =  get_size()[1]/2
	x = get_size()[0]/10*9
	driver.swipe(x1,y1,x,y1)

def swip_up():
    #向左滑动
	x1  = get_size()[0]/2
	y1 =  get_size()[1]/10*9
	x = get_size()[1]/10
	driver.swipe(x1,y1,x1,y)

def swip_down():
    #向左滑动
    x1  = get_size()[0]/2
    y1 =  get_size()[1]/10
    x = get_size()[0]/10*9
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

driver = get_driver()
swip_left()
swip_left()
swip_right()





















