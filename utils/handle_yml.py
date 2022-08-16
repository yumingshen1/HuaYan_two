# /Library/Frameworks/Python.framework/Versions/3.7/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2022/8/16 9:37 AM
# @Author  : YOURNAME
# @FileName: handle_yml.py
# @Software: PyCharm

from utils.handle_path import config_path
import yaml,os

def get_ApiData_yml(fileDir):
    with open(fileDir,'r',encoding='utf-8') as f:
        return yaml.safe_load(f.read())


if __name__ == '__main__':
    fileName = os.path.join(config_path, 'apiConfig.yml')
    print(get_ApiData_yml(fileName))
