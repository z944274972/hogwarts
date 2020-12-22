# !/usr/bin/env python
# @Time    : 2020/12/22 17:12
# @Author  : zhang yu xin
# @Python  : 3.7.5
# @File    : test_demo
# @Project : hogwarts

from appium import webdriver
import pytest

def test_demo():
	# 1\准备参数：告诉appium，你要打开哪个设备上的哪个app。
	desired_caps = {
		# "automationName": "UiAutomator2",  # 使用哪个自动化引擎,appium1.x可以不用写
		"platformName": "Android",  # 使用哪个移动操作系统平台
		"platformVersion": '11',  # 移动操作系统版本
		"deviceName": "emulator-5554",  # 使用的移动设备或模拟器的种类,需要在cmd命令下，敲adb devices查看
		"appPackage": "com.tencent.wework",  # 所要测试的app的包名，获取命令：aapt dump badging apk路径，查看package: name=
		"appActivity": ".launch.LaunchSplashActivity",
		# 所要测试app的入口页面，获取命令：aapt dump badging apk路径，查看launchable-activity: name='
		"noReset": True  # 在此会话之前，请勿重置应用程序状态
	}

	# 2、连接appium server，把启动参数发送
	driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)  # 要讲源代码里提供的端口号改成4723


if __name__ == '__main__':
    pytest.main()