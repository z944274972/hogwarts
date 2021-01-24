# -*- coding: utf-8 -*-
# @Time     :  2021/1/13 20:47
# @Author   :  zhangyuxin
# @Email    :  zhangyuxin.aikebo@bytedance.com
# @File     :  test_demo.py

from selenium import webdriver

class TestData:

    def test_data(self):

        driver = webdriver.Chrome()
        driver.get("https://home.testing-studio.com")
        a = driver.execute_script("return window.performance.timing")
        print(type(a))

        b = driver.execute_script("return JSON.stringify(window.performance.timing)")
        print(type(b))

        print(a["connectEnd"])
        # print(b["connectEnd"])
