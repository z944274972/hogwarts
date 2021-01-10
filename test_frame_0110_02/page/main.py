# -*- coding: utf-8 -*-
# @Time     :  2021/1/9 13:05
# @Author   :  zhangyuxin
# @Email    :  zhangyuxin.aikebo@bytedance.com
# @File     :  main.py

from test_frame_0110_02.page.market import Market
from test_frame_0110_02.page.pre_page import PrePage


class Main(PrePage):

    def goto_market(self):

        # self.find_click(By.XPATH, "//*[@resource-id='com.xueqiu.android:id/post_status']")
        # self.find_click(By.XPATH,"//*[@resource-id='android:id/tabs']//*[@text='行情']")
        self.basepage.load("../page/main.yaml")
        return Market(self.basepage)