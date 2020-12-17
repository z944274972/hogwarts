# -*- coding: utf-8 -*-
# @Time     :  2020/12/17 22:02
# @Author   :  zhangyuxin
# @Email    :  zhangyuxin.aikebo@bytedance.com
# @File     :  test_case_add.py
import time

import pytest
import yaml
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Test_add:

    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)
        self.driver.get("https://work.weixin.qq.com/wework_admin/loginpage_wx?")

    def teardown(self):
        self.driver.quit()

    def test_add(self):
        with open("cookie.yml") as f:
            yaml_data = yaml.safe_load(f)
            for cookie in yaml_data:
                self.driver.add_cookie(cookie)
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#contacts")
        time.sleep(2)
        self.driver.implicitly_wait(5)
        WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@class="js_has_member"]//a[text()="添加成员"]'))).click()
        # driver.find_element_by_xpath('//*[@class="js_has_member"]//a[text()="添加成员"]').click()
        self.driver.find_element_by_id("username").send_keys("admin231")
        self.driver.find_element_by_id("memberAdd_acctid").send_keys("cici232521")
        self.driver.find_element_by_id("memberAdd_phone").send_keys("13252335611")
        self.driver.find_element_by_class_name("js_btn_save").click()
        elements = self.driver.find_elements(By.CSS_SELECTOR, ".member_colRight_memberTable_td:nth-child(2)")
        member = self.get_member(elements)
        print(member)
        assert "admin231" in member


    def get_member(self,elements):
        list = []
        for element in elements:
            list.append(element.get_attribute("title"))
            time.sleep(2)
            return list

    # def test_fuyong(self):
    #     opt = webdriver.ChromeOptions()
    #     opt.debugger_address = "127.0.0.1:9222"
    #     driver = webdriver.Chrome(options=opt)
    #     driver.get("https://work.weixin.qq.com/wework_admin/frame#contacts")
    #     driver.implicitly_wait(5)
    #     WebDriverWait(driver, 10).until(
    #         EC.element_to_be_clickable((By.XPATH, '//*[@class="js_has_member"]//a[text()="添加成员"]'))).click()
    #     # driver.find_element_by_xpath('//*[@class="js_has_member"]//a[text()="添加成员"]').click()
    #     driver.find_element_by_id("username").send_keys("admi21111")
    #     driver.find_element_by_id("memberAdd_acctid").send_keys("cic1i21521")
    #     driver.find_element_by_id("memberAdd_phone").send_keys("13112144612")
    #     driver.find_element_by_class_name("js_btn_save").click()
    #     time.sleep(2)
    #     list = []
    #     elements = driver.find_elements(By.CSS_SELECTOR, ".member_colRight_memberTable_td:nth-child(2)")
    #     for element in elements:
    #         list.append(element.get_attribute("title"))
    #     assert "admi21111" in list
