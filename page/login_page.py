#!/usr/bin/env python
# -*- coding: utf-8 -*-
from util.get_by_local import GetByLocal

class LoginPage:
	"""获取登录页面的所有元素信息"""
	def __init__(self,driver):
		self.g = GetByLocal(driver)

	def get_username_element(self):
		"""获取用户名element信息"""
		user_element = self.g.get_element("username")
		return user_element

	def get_password_element(self):
		"""获取密码element信息"""
		password_element = self.g.get_element("passwd")
		return password_element

	def get_login_bun_element(self):
		"""获取登录按钮element信息"""
		login_btn= self.g.get_element("login_btn")
		return login_btn

	def get_forget_password_element(self):
		"""忘记密码按钮"""
		forget_password_element=self.g.get_element("forget_password")
		return forget_password_element

	def regeister_element(self):
		"""注册按钮"""
		pass

	def get_tost_element(self,message):
		"""断言"""
		tost_element = ("xpath","//*[contains(@text,"+message+")]")


















