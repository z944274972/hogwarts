# !/usr/bin/env python
# @Time    : 2020/12/23 09:49
# @Author  : zhang yu xin
# @Python  : 3.7.5
# @File    : add_party_page
# @Project : hogwarts
import time

from selenium.webdriver.common.by import By

from test_selenium_1220_01.test_web_weixin.page.base_page import BasePage


class AddParty(BasePage):
	_location_party_name = (By.CSS_SELECTOR, '.member_tag_dialog_inputDlg input[name="name"]')
	_location_select_party = (By.CSS_SELECTOR, ".js_toggle_party_list")
	_location_select_name = (By.XPATH, '//form//a[@class="jstree-anchor" and text()="cici"]')
	_location_sure = (By.CSS_SELECTOR, '.ww_dialog_foot .ww_btn_Blue')
	_location_party_list = (By.CSS_SELECTOR, ".jstree-container-ul .jstree-children .jstree-anchor")

	def add_party(self):
		self.find(self._location_party_name).send_keys("zhuolang")
		self.find(self._location_select_party).click()
		self.wait_click(self._location_select_name)
		self.find(self._location_select_name).click()
		self.find(self._location_sure).click()
		time.sleep(1)
		elements = self.finds(*self._location_party_list)
		party_list = [i.text for i in elements]
		return party_list