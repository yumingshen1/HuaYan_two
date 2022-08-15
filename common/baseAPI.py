# /Library/Frameworks/Python.framework/Versions/3.7/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2022/8/15 6:00 PM
# @Author  : YOURNAME
# @FileName: baseAPI.py
# @Software: PyCharm

import requests

class BaseAPI:
    def __int__(self,cookies=None):
        if cookies:
            self.cookies = cookies
        else:
            self.cookies = None


    def request_send(self,method,params=None,json=None,id="",isLogin=False):
        try:
            resp = requests.request(method,url=f'{HOST}{PATH}/{id}',json=json,params=params,cookies=self.cookies)
        except Exception as e:
            raise e