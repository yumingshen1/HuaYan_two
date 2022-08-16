# /Library/Frameworks/Python.framework/Versions/3.7/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2022/8/15 6:00 PM
# @Author  : YOURNAME
# @FileName: baseAPI.py
# @Software: PyCharm

import requests,os
from configs.configs import Configs
from utils.handle_path import config_path
from utils.handle_yml import get_ApiData_yml

class BaseAPI:
    def __init__(self,cookies=None):
        if cookies:
            self.cookies = cookies
            self.space = self.cookies['X-Space-Id']
        else:
            self.cookies = None
        ##获得业务对应的数据模板
        self.data = get_ApiData_yml(os.path.join(config_path,'apiConfig.yml'))[self.__class__.__name__]

    def request_send(self,method,params=None,json=None,id="",isLogin=False):
        PATH = self.data['path']
        try:
            resp = requests.request(method,url=f'{Configs.HOST}{PATH}/{id}',json=json,params=params,cookies=self.cookies)
            if isLogin:
                return resp #登录 返回响应体
            else:
                return resp.json() #非登录，返回响应json数据

        except Exception as e:
            raise e

    def add(self,**kwargs):
        payload = self.data['add']
        kwargs['space'] = self.space
        payload.update(kwargs)
        resp = self.request_send('POST',json=payload)
        return resp['value'][0]


    def delete(self,id):
        return self.request_send('DELETE',id=id)

    def update(self,id,**kwargs):
        payload = self.data['update']
        kwargs['space'] = self.space
        payload['$set'].update(kwargs)
        resp = self.request_send('PUT',id=id,json=payload)
        return resp

    def query(self,**kwargs):
        resp = self.request_send('GET',params=kwargs)
        return resp['value']


    def delete_all_items(self):
        items = self.query()
        for item in items:
            self.delete(item['_id'])
