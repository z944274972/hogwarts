# !/usr/bin/env python
# @Time    : 2020/12/22 17:12
# @Author  : zhang yu xin
# @Python  : 3.7.5
# @File    : test_demo
# @Project : hogwarts
from time import sleep

from appium import webdriver
import pytest
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.wait import WebDriverWait


class TestDaka:

	def setup(self):
		# 1\准备参数：告诉appium，你要打开哪个设备上的哪个app。
		desired_caps = {
			# "automationName": "UiAutomator2",  # 使用哪个自动化引擎,appium1.x可以不用写
			"platformName": "Android",  # 使用哪个移动操作系统平台
			"platformVersion": '6.0.1',  # 移动操作系统版本
			"deviceName": "127.0.0.1:7555",  # 使用的移动设备或模拟器的种类,需要在cmd命令下，敲adb devices查看
			"appPackage": "com.tencent.wework",  # 所要测试的app的包名，获取命令：aapt dump badging apk路径，查看package: name=
			"appActivity": ".launch.LaunchSplashActivity",
			# 所要测试app的入口页面，获取命令：aapt dump badging apk路径，查看launchable-activity: name='
			"noReset": True,  # 在此会话之前，请勿重置应用程序状态
			"settings[waitForIdleTimeout]":0
		}
		# {
		# 	"platformName": "Android",
		# 	"appPackage": "com.tencent.wework",
		# 	"appActivity": ".launch.LaunchSplashActivity",
		# 	"noReset": True
		# }

		# 2、连接appium server，把启动参数发送
		self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)  # 要讲源代码里提供的端口号改成4723
		self.driver.implicitly_wait(30)


	def teardown(self):
		self.driver.quit()


	def test_daka(self):

		self.driver.find_element(MobileBy.XPATH,"//*[@text='工作台']").click()
		self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,'new UiScrollable(new UiSelector().scrollable(true).instance(0)).scrollIntoView(new UiSelector().text("打卡").instance(0));').click()
		self.driver.find_element(MobileBy.XPATH,"//*[@text='外出打卡']").click()
		self.driver.find_element(MobileBy.XPATH,"//*[contains(@text,'次外出')]").click()
		WebDriverWait(self.driver,10).until(lambda x :"外出打卡成功" in x.page_source)
		print(self.driver.page_source)
		assert "外出打卡成功" in self.driver.page_source


if __name__ == '__main__':
    pytest.main()