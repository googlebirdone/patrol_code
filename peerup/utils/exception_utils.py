# -*- coding:utf-8 -*-
# @Author:guqingjun
# @Time  :2025/1/16 16:44
# @File  :exception_utils.py
import inspect
import time

import allure


def exception_record(func):
    def inner(*args, **kwargs):
        for name, item in inspect.getmembers(args[-1]):
            if not name.startswith("_") and hasattr(item, "driver"):
                driver = item.driver

        try:
            result = func(*args, **kwargs)
            return result
        except Exception as e:
            timestamp = int(time.time())
            image_path = f"../logs/image_{timestamp}.PNG"
            driver.save_screenshot(image_path)
            allure.attach.file(image_path, name="image", attachment_type=allure.attachment_type.PNG)
            raise e

    return inner
