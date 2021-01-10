# -*- coding: utf-8 -*-
# @Time     :  2021/1/9 13:10
# @Author   :  zhangyuxin
# @Email    :  zhangyuxin.aikebo@bytedance.com
# @File     :  market.py

from test_frame_0110_02.page.pre_page import PrePage
from test_frame_0110_02.page.search import Search


class Market(PrePage):

    def goto_search(self):

        # self.find_click(By.XPATH,"//*[@resource-id='com.xueqiu.android:id/action_search']")
        self.basepage.load("../page/market.yaml")
        return Search(self.basepage)