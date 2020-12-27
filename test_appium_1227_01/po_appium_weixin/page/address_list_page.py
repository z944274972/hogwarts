# -*- coding: utf-8 -*-
# @Time     :  2020/12/27 19:40
# @Author   :  zhangyuxin
# @Email    :  zhangyuxin.aikebo@bytedance.com
# @File     :  address_list_page.py
from appium.webdriver.common.mobileby import MobileBy

from test_appium_1227_01.po_appium_weixin.page.base_page import BasePage
from test_appium_1227_01.po_appium_weixin.page.member_invite_menu_page import MemberInviteMenu


class AddressList(BasePage):

    def click_add_member(self):
        '''增加成员'''

        # self.scroll_find_click("添加成员")
        self.swip_find_click(MobileBy.XPATH,'//*[@text="添加成员"]')

        return MemberInviteMenu(self.driver)