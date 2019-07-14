#! /usr/bin/env python
#coding=utf-8
#author=zgd
from page.login_page import LoginPage
class LoginHandle:
    """登录页面操作层"""
    def __init__(self,driver):
        self.login_page = LoginPage()

    def send_username(self,user):
        """请输入用户名"""
        self.login_page.get_username_element().send_keys(user)

    def seng_passwd(self,password):
        """输入密码"""
        self.login_page.get_password_element().send_keys(password)

    def click_login(self):
        """登录按钮"""
        self.login_page.get_login_bun_element().click()

    def click_forget_passwd(self):
        """忘记密码"""
        self.login_page.get_forget_password_element().click()













