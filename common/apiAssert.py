# /Library/Frameworks/Python.framework/Versions/3.7/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2022/8/16 3:07 PM
# @Author  : YOURNAME
# @FileName: apiAssert.py
# @Software: PyCharm
from typing import Iterable


class ApiAssert:
    @classmethod
    def api_Assert(cls,result,condition,exp_result):
        try:
            assert_type = {
                "==":result == exp_result,
                "!=":result != exp_result,
                ##in not in  是序列，需要判断是否是序列，在进行校验，
                "in":result in exp_result if isinstance(exp_result,Iterable) else False,
                "not in":result not in exp_result if isinstance(exp_result,Iterable) else False
            }
            if condition in assert_type:
                assert assert_type[condition]
            else:
                raise AssertionError('请输入正确断言')
        except Exception as e:
            raise e

if __name__ == '__main__':
    ApiAssert.api_Assert(5,'in',(2.2,4,6,10,5))