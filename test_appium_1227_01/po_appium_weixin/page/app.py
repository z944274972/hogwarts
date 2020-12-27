# -*- coding: utf-8 -*-
# @Time     :  2020/12/27 19:58
# @Author   :  zhangyuxin
# @Email    :  zhangyuxin.aikebo@bytedance.com
# @File     :  app.py
from appium import webdriver

from test_appium_1227_01.po_appium_weixin.page.base_page import BasePage
from test_appium_1227_01.po_appium_weixin.page.main_page import Main



class App(BasePage):

    def start(self):

        if self.driver is None :
            desired_caps = {
                # "automationName": "UiAutomator2",  # 使用哪个自动化引擎,appium1.x可以不用写
                "platformName": "Android",  # 使用哪个移动操作系统平台
                "platformVersion": '6.0.1',  # 移动操作系统版本
                "deviceName": "127.0.0.1:7555",  # 使用的移动设备或模拟器的种类,需要在cmd命令下，敲adb devices查看
                "appPackage": "com.tencent.wework",  # 所要测试的app的包名，获取命令：aapt dump badging apk路径，查看package: name=
                "appActivity": ".launch.LaunchSplashActivity",
                # 所要测试app的入口页面，获取命令：aapt dump badging apk路径，查看launchable-activity: name='
                "noReset": True,  # 在此会话之前，请勿重置应用程序状态
                "settings[waitForIdleTimeout]": 0}

            self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

        else:
            self.driver.launch_app()

        self.driver.implicitly_wait(30)

    def goto_main(self):
        return Main(self.driver)