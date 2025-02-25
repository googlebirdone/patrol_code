# -*- coding:utf-8 -*-
# @Author:guqingjun
# @Time  :2025/1/6 18:43
# @File  :home_page.py
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from peerup.page_source.base_page import BasePage
from peerup.utils.log_utils import logger


class HomePage(BasePage):
    _add_button = (By.CSS_SELECTOR, 'img[class*="add"]')
    _project_name = (By.CSS_SELECTOR, 'input[placeholder*="项目名称"]')
    _project_submit = (By.CSS_SELECTOR, 'button[type="submit"]')
    _project_check = (By.CSS_SELECTOR, '[class*="anticon-check"]')

    _project = (By.XPATH, '//*[text()="项目"]')

    def add_project(self, project_name):
        logger.info("新增项目")
        # 点击添加按钮
        self.click_element(*self._add_button)
        # todo 输入项目信息
        self.input_key(project_name, *self._project_name)
        WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(self._project_submit))
        self.click_element(*self._project_submit)
        # 防止互相导入导致无法使用问题
        from peerup.page_source.project_page import ProjectPage
        return ProjectPage(self.driver)

    def select_project(self):
        logger.info("选择项目")
        self.click_element(*self._projectName)
        from peerup.page_source.project_page import ProjectPage
        return ProjectPage(self.driver)

    def auto2project(self):
        logger.info("自动跳转到了项目页")
        from peerup.page_source.project_page import ProjectPage
        return ProjectPage(self.driver)

    def get_project_result(self):
        ele = WebDriverWait(self.driver, 10).until(
            expected_conditions.visibility_of_element_located(self._project_check))

        msg = ele.text
        self.get_page_png()
        logger.info(f"页面：{self.get_page_source()}")
        logger.info(f"项目添加的结果：{msg}")
        return msg
