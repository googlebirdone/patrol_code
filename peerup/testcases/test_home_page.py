# -*- coding:utf-8 -*-
# @Author:guqingjun
# @Time  :2025/1/7 17:24
# @File  :test_home_page.py
import inspect
import sys
import time

import allure
import pytest

from peerup.page_source.login_page import LoginPage
from pytest import fixture, mark

from peerup.utils.exception_utils import exception_record


class TestHomePage:
    def setup_class(self):
        self.home = LoginPage().login()

    @mark.parametrize("project_name,res", [("test", "创建成功")])
    def test_add(self, project_name, res):
        """
        登录页登录==>首页添加项目==>项目页跳转回首页==>检查项目页新增成功
        :param project_name:
        :param res:
        :return:
        """
        result = self.home.add_project(project_name).get_project_result()
        assert result == res

    @mark.parametrize(argnames="content,level", argvalues=[("my name is 谷歌", 0), ("my name is google", 1)])
    def test_content(self, content, level):
        """
        deng
        :param content:
        :param level:
        :return:
        """
        @exception_record
        def sub_content(content, level, self=self):
            result = self.home.auto2project().add_item().title_add("介绍").content_add(
                content, level).get_content_result(level)
            return result

        assert sub_content(content, level, self) == f"h{level + 1}"
