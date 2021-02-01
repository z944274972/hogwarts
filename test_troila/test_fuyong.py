# !/usr/bin/env python
# @Time    : 2021/2/1 09:25
# @Author  : zhang yu xin
# @Python  : 3.7.5
# @File    : test_fuyong
# @Project : hogwarts
import time

import yaml
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class TestFuyong:

	def test_save(self):
		'''存储cookie操作'''
		opt = webdriver.ChromeOptions()
		opt.debugger_address = "127.0.0.1:9222"
		driver = webdriver.Chrome(options=opt)
		driver.implicitly_wait(5)
		driver.get("http://172.28.31.3/admin/login?redirect=%2Froles-users")
		time.sleep(10)
		# 间歇操作自行登录进行存储cookies
		cookie = driver.get_cookies()
		with open('./cookie.yaml','w',encoding='utf-8') as f:
			yaml.dump(cookie,f)


	def test_login(self):
		'''使用cookie复用'''
		driver = webdriver.Chrome()
		driver.implicitly_wait(5)
		driver.get("http://172.28.31.3/admin/support-module")
		with open("./cookie.yaml",encoding="utf-8") as f:
			yaml_data = yaml.safe_load(f)
			for cookie in yaml_data:
				driver.add_cookie(cookie)
		driver.get("http://172.28.31.3/admin/defense-manage?activity_type=cad")
		time.sleep(5)

