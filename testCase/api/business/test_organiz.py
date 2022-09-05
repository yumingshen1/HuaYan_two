# /Library/Frameworks/Python.framework/Versions/3.7/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2022/8/17 10:32 AM
# @Author  : YOURNAME
# @FileName: test_organiz.py
# @Software: PyCharm
import pytest
from common.apiAssert import ApiAssert

@pytest.fixture()
def tc0001_fixtrue(empty_orgs):
    print('---test_tc0001数据初始化---')
    api_org = empty_orgs
    yield api_org
    api_org.delete(add_org['_id'])
    print('---test_tc001数据清除---')


def test_tc0001(tc0001_fixtrue):

    global add_org
    #获得部门实例
    api_org = tc0001_fixtrue
    #添加部门
    add_org = api_org.add(name='Test_organiz')
    api_org_list = api_org.query()
    #断言
    ApiAssert.api_Assert(add_org,'in',api_org_list)

if __name__ == '__main__':
    pytest.main([__file__,'-sv'])
