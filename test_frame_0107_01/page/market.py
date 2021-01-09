# -*- coding: utf-8 -*-
# @Time     :  2021/1/9 13:10
# @Author   :  zhangyuxin
# @Email    :  zhangyuxin.aikebo@bytedance.com
# @File     :  market.py
from selenium.webdriver.common.by import By

from test_frame_0107_01.base_page import BasePage
from test_frame_0107_01.page.search import Search


class Market(BasePage):

    def goto_search(self):


        self.find_click(By.XPATH,"//*[@resource-id='com.xueqiu.android:id/action_search']")
        return Search(self.driver)