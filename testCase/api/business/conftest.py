# /Library/Frameworks/Python.framework/Versions/3.7/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2022/8/17 10:30 AM
# @Author  : YOURNAME
# @FileName: conftest.py
# @Software: PyCharm

import pytest
from libs.api.login import LoginApi
from libs.api.organiz import OrganizApi

'''
登录--部门初始化
'''
@pytest.fixture(scope='session',autouse=False)
def login_init():
    print('----登录初始化-------')
    login_cookies = LoginApi().login(username='807145107@qq.com',password='123456',getcookies=True)
    yield login_cookies
    print('----登录初始化完成-----')

@pytest.fixture(scope='session')
def empty_orgs(login_init):
    print('----清除所有部门(不含总部门)-----')
    cookies = login_init
    org = OrganizApi(cookies)
    org.delete_all_times()
    yield org
    print('----清除所有部门完成(不含总部门)----')

if __name__ == '__main__':
    pytest.main([__file__,'-s'])