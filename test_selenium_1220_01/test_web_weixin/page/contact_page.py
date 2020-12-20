# -*- coding: utf-8 -*-
# @Time     :  2020/12/20 14:40
# @Author   :  zhangyuxin
# @Email    :  zhangyuxin.aikebo@bytedance.com
# @File     :  contact_page.py
from selenium.webdriver.common.by import By

from test_selenium_1220_01.test_web_weixin.page.base_page import BasePage


class ContactPage(BasePage):

    def add_member(self):
        '''添加成员'''
        pass

    def get_member(self):
        '''获取成员列表'''
        elements = self.driver.find_elements(By.CSS_SELECTOR,".member_colRight_memberTable_td:nth-child(2)")
        member_list = []
        for i in elements:
            member_list.append(i.text)
        return member_list

