# -*- coding: utf-8 -*-
# @Time     :  2020/12/20 14:23
# @Author   :  zhangyuxin
# @Email    :  zhangyuxin.aikebo@bytedance.com
# @File     :  index_page.py
from test_selenium_1220_01.po_object_demo.page.login_page import LoginPage
from test_selenium_1220_01.po_object_demo.page.register_page import RegisterPage


class IndexPage:


    def goto_login(self):
        '''
        跳转至登录界面
        '''
        return LoginPage()

    def goto_register(self):
        '''
        跳转至注册界面
        '''
        return RegisterPage()