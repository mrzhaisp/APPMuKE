#!/usr/bin/env python
# -*- coding: utf-8 -*-
from util.read_ini import ReadIni
class GetByLocal:
	"""从read_ini里取到数据，截取取到的数据直接封装到  find_element 里"""
	def __init__(self,driver):
		self.driver = driver
		self.r = ReadIni()

	def get_element(self,key):
		#拿到read_ini中读取到的数据
		value = self.r.get_value(key)
		#拿到 读取出来的数据id>cn.com.open.mooc:id/accountEdit  并且分割
		by = value.split('>')[0]
		local = value.split('>')[1]
		#分割后传入到下边定位方式中
		if by == "id":
			return 	self.driver.find_element_by_id(local)
		elif by == "className":
			return driver.find_elements_by_class_name(local)
		elif by == "xpath":
			return self.driver.find_element_by_xpath(local)
















