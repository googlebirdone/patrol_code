# -*- coding:utf-8 -*-
# @Author:guqingjun
# @Time  :2025/1/6 20:10
# @File  :project_page.py
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from peerup.page_source.base_page import BasePage
from peerup.utils.log_utils import logger


class ProjectPage(BasePage):
    _project_check = (By.CSS_SELECTOR, '[class*="message-notice-content"]')
    _item_add = (By.XPATH, '//*[text()="新建"]')
    _item = (By.XPATH, '//*[text()="笔记"]')
    _doc_name = (By.XPATH, '//*[text()="未命名文档"]')

    _tag_add = (By.CSS_SELECTOR, '[class*="tags-item-add"]')
    _title_add = (By.CSS_SELECTOR, '[data-placeholder="请输入标题"]')
    _content_add = (By.CSS_SELECTOR, '[data-content-type="paragraph"]')
    _content = (By.XPATH, '//h3')

    _level_add = (By.CSS_SELECTOR, '.block-menu-wrapper')
    _level = (By.XPATH, '//*[contains(@class,"icon-workspace-h")]')
    _check_msg = "创建成功"

    def add_item(self):
        try:
            self.click_element(*self._item_add)
            self.click_element(*self._item)
            # todo 拆出来文档选择
            # self.click_element(*self._doc_name)
            return self
        except Exception as e:
            logger.info(e)
        finally:
            self.get_page_png()

    def tag_add(self, tag):
        ele = self.search_element(*self._tag_add)
        WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(ele))
        self.input_key(tag, *self._tag_add)
        return self

    def title_add(self, title):
        try:
            WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(self._title_add))
        except Exception as e:
            logger.info(e)
        finally:
            self.input_key(title, *self._title_add)
            return self

    def content_add(self, content, level):
        self.hover(self._content_add)
        self.click_element(*self._level_add)
        self.click_element(*self._level, index=level)
        # 此处总提示出现了iframe的情况,找不到元素；换成js的方式
        js_command = f"document.querySelector('h{level + 1}').textContent='{content}'"
        self.execute_js(js_command)
        return self

    def get_content_result(self, level):
        _content = (By.XPATH, f'//h{level + 1}')
        self.hover(_content)
        phase = self.search_element(*_content)
        return phase.tag_name

    def get_project_result(self):
        res = WebDriverWait(self.driver, 10).until(
            self.alert(self._project_check, self._check_msg))
        ele = self.search_element(*self._project_check)
        msg = ele.text
        logger.info(f"页面：{self.get_page_source()}")
        logger.info(f"项目添加的结果：{msg}")
        return msg
