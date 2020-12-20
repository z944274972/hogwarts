# -*- coding: utf-8 -*-
# @Time     :  2020/12/20 14:41
# @Author   :  zhangyuxin
# @Email    :  zhangyuxin.aikebo@bytedance.com
# @File     :  add_member.py
from selenium.webdriver.common.by import By

from test_selenium_1220_01.test_web_weixin.page.base_page import BasePage
from test_selenium_1220_01.test_web_weixin.page.contact_page import ContactPage


class AddMember(BasePage):

    def add_member(self):

        self.driver.find_element(By.ID,"username").send_keys("admin231")
        self.driver.find_element(By.ID,"memberAdd_acctid").send_keys("cici232521")
        self.driver.find_element(By.ID,"memberAdd_phone").send_keys("13252335611")
        self.driver.find_element(By.CSS_SELECTOR,".js_btn_save").click()
        return ContactPage(self.driver)