# -*- coding:utf-8 -*-
# @Author:guqingjun
# @Time  :2025/1/7 17:51
# @File  :conftest.py

def pytest_collection_modifyitems(items):
    for item in items:
        # 重新编码name和nodeid，以正确显示中文字符
        item.name = item.name.encode("utf-8").decode("unicode_escape")
        item._nodeid = item.nodeid.encode("utf-8").decode("unicode_escape")
