# -*- coding:utf-8 -*-
# @Author:guqingjun
# @Time  :2025/1/14 22:58
# @File  :test_project_page.py
import allure
from pytest import mark, fixture

from peerup.page_source.login_page import LoginPage


class TestProjectPage:
    def setup_class(self):
        self.home = LoginPage().login()

    @mark.parametrize("content,level", [("my name is 谷歌", 0)])
    @allure.attach.file()
    def test_content(self, content, level):
        result = self.home.select_project().add_item().title_add("介绍").content_add(
            content, level).get_content_result(level)
        print(result)
