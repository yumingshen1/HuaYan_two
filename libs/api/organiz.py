# /Library/Frameworks/Python.framework/Versions/3.7/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2022/8/16 10:32 AM
# @Author  : YOURNAME
# @FileName: organiz.py
# @Software: PyCharm

from  common.baseAPI import BaseAPI

class OrganizApi(BaseAPI):
    def __init__(self,cookies):
        super(OrganizApi, self).__init__(cookies) #调用父类初始化
        #获得总部门
        orgList = self.query()
        self.top_parentID = orgList[0]['_id']
        print('总id:',self.top_parentID)

    def add(self,**kwargs):
        if "parent" not in kwargs:
            kwargs['parent'] = self.top_parentID
        return super(OrganizApi, self).add(**kwargs)
        

    def update(self,id,**kwargs):
        if 'parent' not in kwargs:
            kwargs['parent'] = self.top_parentID
        return super(OrganizApi, self).update(id=id,**kwargs)

    ## 全部删除，过滤总部门， 从子部门开始删除(倒着)，
    def delete_all_times(self):
        items = self.query()[1:]
        for item in items[::-1]:
            self.delete(item['_id'])

