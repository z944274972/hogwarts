# -*- coding: utf-8 -*-
# @Time     :  2020/12/27 19:41
# @Author   :  zhangyuxin
# @Email    :  zhangyuxin.aikebo@bytedance.com
# @File     :  contact_add_page.py
from appium.webdriver.common.mobileby import MobileBy

from test_appium_1227_01.po_appium_weixin.page.base_page import BasePage


class ContactAdd(BasePage):

    def add_contact(self):
        '''成员信息编辑'''

        self.find_sendkeys(MobileBy.XPATH, '//*[contains(@text,"姓名")]/..//*[@text="必填"]',"小虎牙lyy")
        self.find_click(MobileBy.XPATH, '//*[contains(@text,"性别")]/..//*[@text="男"]')
        self.wait_for(MobileBy.XPATH,'//*[@text="女"]')
        self.find_click(MobileBy.XPATH, '//*[@text="女"]')
        self.find_sendkeys(MobileBy.XPATH, '//*[contains(@text,"手机")]/..//*[@text="手机号"]',"18232345678")
        self.find_click(MobileBy.XPATH, '//*[@text="保存"]')
        return True