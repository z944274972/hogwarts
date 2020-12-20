# -*- coding: utf-8 -*-
# @Time     :  2020/12/20 14:41
# @Author   :  zhangyuxin
# @Email    :  zhangyuxin.aikebo@bytedance.com
# @File     :  add_member.py
from selenium.webdriver.common.by import By

from test_selenium_1220_01.test_web_weixin.page.base_page import BasePage
from test_selenium_1220_01.test_web_weixin.page.contact_page import ContactPage


class AddMember(BasePage):

    _location_username = (By.ID,"username")
    _location_acctid = (By.ID,"memberAdd_acctid")
    _location_Add_phone = (By.ID,"memberAdd_phone")
    _location_save = (By.CSS_SELECTOR,".js_btn_save")

    # def add_member(self):
    #
    #     self.find(*self._location_username).send_keys("admin3")
    #     self.find(*self._location_acctid).send_keys("cici3")
    #     self.find(*self._location_Add_phone).send_keys("13252145614")
    #     self.find(*self._location_save).click()
    #     return ContactPage(self.driver)

    def add_member(self):
        """添加成员操作
        :return:
        """
        self.driver.find_element(*self._location_username).send_keys("赫敏4")
        self.driver.find_element(*self._location_acctid).send_keys("023")
        self.driver.find_element(*self._location_Add_phone).send_keys("13127778882")
        self.driver.find_element(By.CSS_SELECTOR, ".js_btn_save").click()
        return ContactPage(self.driver)

    def add_member_fail(self,accid,phone):
        self.find(*self._location_username).send_keys("admin231")
        self.find(*self._location_acctid).send_keys(accid)
        self.find(*self._location_Add_phone).send_keys(phone)
        self.find(*self._location_save).click()
        # error_message = self.find(By.CSS_SELECTOR,"").text
        # phone_message = self.find(By.CSS_SELECTOR,"").text
        res = self.finds(By.CSS_SELECTOR,".ww_inputWithTips_tips")
        error_list = [i.text for i in res]
        return error_list