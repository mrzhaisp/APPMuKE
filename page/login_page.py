#!/usr/bin/env python
# -*- coding: utf-8 -*-
from util.get_by_local import GetByLocal
from appium import webdriver
class LoginPage:
	def __init__(self):
		self.driver = webdriver()

	def get_username_element(self):
		return self.driver.fin






























