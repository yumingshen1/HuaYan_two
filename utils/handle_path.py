# /Library/Frameworks/Python.framework/Versions/3.7/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2022/8/16 9:38 AM
# @Author  : YOURNAME
# @FileName: handle_path.py
# @Software: PyCharm

import os
#工程路径-绝对路径
product_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

#config
config_path = os.path.join(product_path,'configs')

#casedata
caseData_path = os.path.join(product_path,'data')

#log_path
log_path = os.path.join(product_path,'outFiles/log')


# print(product_path)