# -*- coding: utf-8 -*-
# @Time     :  2021/1/9 13:05
# @Author   :  zhangyuxin
# @Email    :  zhangyuxin.aikebo@bytedance.com
# @File     :  main.py
from selenium.webdriver.common.by import By

from test_frame_0110_01.base_page import BasePage
from test_frame_0110_01.page.market import Market


class Main(BasePage):

    def goto_market(self):

        # self.find_click(By.XPATH, "//*[@resource-id='com.xueqiu.android:id/post_status']")
        # self.find_click(By.XPATH,"//*[@resource-id='android:id/tabs']//*[@text='行情']")
        self.load("../page/main.yaml")
        return Market(self.driver)