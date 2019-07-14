#! /usr/bin/env python
#coding=utf-8
#author=zgd
from handle.login_handle import LoginHandle

class LoginBussiness:
    def __init__(self):
        self.lohaddler=LoginHandle(driver)

    def login_pass(self):
        """登录成功"""
        self.lohaddler.send_username("18141923568")
        self.lohaddler.seng_passwd("Cmcc@121122")
        self.lohaddler.click_login()

    def login_faileed(self):
        """登录失败"""
        self.lohaddler.send_username("18141923568")
        self.lohaddler.seng_passwd("121122")
        self.lohaddler.click_login()




















