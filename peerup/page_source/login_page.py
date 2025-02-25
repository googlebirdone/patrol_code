# -*- coding:utf-8 -*-
# @Author:guqingjun
# @Time  :2025/1/6 17:43
# @File  :login_page.py
from selenium.webdriver.common.by import By
from peerup.page_source.base_page import BasePage


class LoginPage(BasePage):
    _Base_Url = "https://www.peerup.com/login"
    _UserName = (By.CSS_SELECTOR, '[type="text"]')
    _PassWord = (By.CSS_SELECTOR, '[type="password"]')
    _Agree = (By.CSS_SELECTOR, '[type="checkbox"]')
    _Login = (By.CSS_SELECTOR, '[type="submit"]')
    _username = "guqingjunbirdone@gmail.com"
    _password = "google!QAW#@335"

    def login(self, username=_username, password=_password):
        """
        登录成功方法
        :param username:
        :param password:
        :return: 首页
        """
        self.input_key(username, *self._UserName)
        self.input_key(password, *self._PassWord)
        self.click_element(*self._Agree)
        self.click_element(*self._Login)
        from peerup.page_source.home_page import HomePage
        return HomePage(self.driver)

    def login_fail(self, username, password):
        """
        登录失败方法
        :return: 登录页
        """
        self.input_key(username, *self._UserName)
        self.input_key(password, *self._PassWord)
        self.click_element(*self._Agree)
        self.click_element(*self._Login)
        return LoginPage(self.driver)

    def judge_fail(self):
        """
        判定登录失败
        :return:
        """
        return self.driver.title
