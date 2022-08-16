# /Library/Frameworks/Python.framework/Versions/3.7/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2022/8/16 10:27 AM
# @Author  : YOURNAME
# @FileName: login.py
# @Software: PyCharm

from  common.baseAPI import BaseAPI

class LoginApi(BaseAPI):

    def __create_data(self,username,password):
        return {"user":{"email":username},"password":password,"code":"","locale":"zh- cn"}

    def login(self,username,password,getcookies=False):
        payload = self.__create_data(username,password)
        resp = self.request_send('POST',json=payload,isLogin=True)
        if getcookies:
            return resp.cookies
        else:
            return resp.json()

if __name__ == '__main__':
    resp = LoginApi().login(username='807145107@qq.com',password='123456')
    print('----',resp)