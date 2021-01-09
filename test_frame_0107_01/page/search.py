# -*- coding: utf-8 -*-
# @Time     :  2021/1/9 13:12
# @Author   :  zhangyuxin
# @Email    :  zhangyuxin.aikebo@bytedance.com
# @File     :  search.py
from selenium.webdriver.common.by import By

from test_frame_0107_01.base_page import BasePage


class Search(BasePage):

    def search(self):

        self.find(By.XPATH,"//*[@resource-id='com.xueqiu.android:id/search_input_text']").send_keys("xxxxx")
        return True
