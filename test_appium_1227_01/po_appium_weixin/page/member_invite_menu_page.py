# -*- coding: utf-8 -*-
# @Time     :  2020/12/27 19:41
# @Author   :  zhangyuxin
# @Email    :  zhangyuxin.aikebo@bytedance.com
# @File     :  member_invite_menu_page.py
from appium.webdriver.common.mobileby import MobileBy

from test_appium_1227_01.po_appium_weixin.page.base_page import BasePage
from test_appium_1227_01.po_appium_weixin.page.contact_add_page import ContactAdd


class MemberInviteMenu(BasePage):


    def add_member_manual(self):
        '''手动添加成员信息'''

        self.find_click(MobileBy.XPATH,"//*[@text='手动输入添加']")

        return ContactAdd(self.driver)