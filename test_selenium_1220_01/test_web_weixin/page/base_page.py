# -*- coding: utf-8 -*-
# @Time     :  2020/12/20 14:59
# @Author   :  zhangyuxin
# @Email    :  zhangyuxin.aikebo@bytedance.com
# @File     :  base_page.py
import yaml
from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver


class BasePage:

    def __init__(self,base_driver=None):

        base_driver : WebDriver
        if base_driver is None:
            self.driver = webdriver.Chrome()
            self.driver.maximize_window()
            self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
            self.__cookie_login()
        else:
            self.driver = base_driver

        self.driver.implicitly_wait(5)

    def __cookie_login(self):

        with open("../testcases/cookie.yml", encoding="UTF-8") as f:
            yaml_data = yaml.safe_load(f)
            for cookie in yaml_data:
                if "expiry" in cookie.keys():
                    del cookie["expiry"]
                self.driver.add_cookie(cookie)
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")