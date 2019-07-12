#!/usr/bin/env python
# -*- coding: utf-8 -*-
import configparser

class ReadIni:
    """读取ini内的文件"""
    def __init__(self,filepath=None):
        """默认传入的ini文件路径"""
        if filepath == None:
            self.filepath = "../config/localElement.ini"
        else:
            self.filepath=filepath
        #初始化就调用读取出来的内容
        self.data = self.readini()

    def readini(self):
        """读取配置文件"""
        read_ini = configparser.ConfigParser()
        read_ini.read(self.filepath,encoding="UTF-8")
        return read_ini


    def get_value(self,key,section=None):
        if section == None:
            section = 'login_element'
        try:
            value =  self.data.get(section,key)
            return value
        except:
            value = None
        return value

# if __name__ == '__main__':
#     r = ReadIni()
#     print(r.get_value("zhanghao"))






