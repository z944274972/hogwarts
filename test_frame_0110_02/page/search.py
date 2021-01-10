# -*- coding: utf-8 -*-
# @Time     :  2021/1/9 13:12
# @Author   :  zhangyuxin
# @Email    :  zhangyuxin.aikebo@bytedance.com
# @File     :  search.py

from test_frame_0110_02.page.pre_page import PrePage


class Search(PrePage):


    def search(self):

        # self.find(By.XPATH,"//*[@resource-id='com.xueqiu.android:id/search_input_text']").send_keys("xxxxx")
        self.basepage.load("../page/search.yaml")
        return True
