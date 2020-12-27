# -*- coding: utf-8 -*-
# @Time     :  2020/12/27 19:40
# @Author   :  zhangyuxin
# @Email    :  zhangyuxin.aikebo@bytedance.com
# @File     :  main_page.py
from appium.webdriver.common.mobileby import MobileBy

from test_appium_1227_01.po_appium_weixin.page.address_list_page import AddressList
from test_appium_1227_01.po_appium_weixin.page.base_page import BasePage


class Main(BasePage):


    def goto_contact(self):
        '''进入通讯录'''

        self.find_click(MobileBy.XPATH,
                                 '//*[@resource-id="com.tencent.wework:id/elq" and @text="通讯录"]')
        return AddressList(self.driver)

