# -*- coding:utf-8 -*-
# @Author:guqingjun
# @Time  :2025/1/6 17:44
# @File  :base_page.py
import time

import allure
import pytest
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    __base_url = "https://www.peerup.com/login"

    def __init__(self, driver=None):
        if not driver:
            self.driver = webdriver.Chrome()
            self.driver.get(self.__base_url)
            self.driver.implicitly_wait(3)
            self.driver.maximize_window()
        else:
            self.driver: WebDriver = driver

    def search_element(self, by, locator=None):
        if locator:
            return self.driver.find_element(by, locator)
        else:
            return self.driver.find_element(*by)

    def search_elements(self, by, locator=None):
        if locator:
            return self.driver.find_elements(by, locator)
        else:
            return self.driver.find_elements(*by)

    def click_element(self, by, locator=None, index=None):
        if index:
            ele = self.search_elements(by, locator)[index]
        else:
            ele = self.search_element(by, locator)
        ele.click()

    def input_key(self, value, by, locator=None):
        ele = self.search_element(by, locator)
        ele.clear()
        ele.send_keys(value)

    def get_page_source(self):
        # source = self.driver.page_source
        url = self.driver.current_url
        return url

    def get_page_png(self):
        # todo 处理图片路径
        self.driver.save_screenshot(fr"..\logs\{time.strftime('%Y%m%d%H%M%S')}.png")

    def alert(self, locator, expected_text):
        def inner(driver: WebDriver):
            ele = driver.find_element(*locator)
            return ele.text == expected_text

        return inner

    def execute_js(self, command, result=False):
        if result:
            return 
        self.driver.execute_script(f"{command}")

    def hover(self, locator):
        action = ActionChains(self.driver)
        ele = self.search_element(*locator)
        action.move_to_element(ele).perform()



