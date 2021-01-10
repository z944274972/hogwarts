# -*- coding: utf-8 -*-
# @Time     :  2020/12/27 19:58
# @Author   :  zhangyuxin
# @Email    :  zhangyuxin.aikebo@bytedance.com
# @File     :  app.py
from appium import webdriver

from test_frame_0110_01.base_page import BasePage
from test_frame_0110_01.page.main import Main



class App(BasePage):

    def start(self):

        if self.driver is None :
            desired_caps = {
                # "automationName": "UiAutomator2",  # 使用哪个自动化引擎,appium1.x可以不用写
                "platformName": "Android",  # 使用哪个移动操作系统平台
                "platformVersion": '6.0.1',  # 移动操作系统版本
                "deviceName": "127.0.0.1:7555",  # 使用的移动设备或模拟器的种类,需要在cmd命令下，敲adb devices查看
                "appPackage": "com.xueqiu.android",  # 所要测试的app的包名，获取命令：aapt dump badging apk路径，查看package: name=
                "appActivity": ".view.WelcomeActivityAlias",
                # 所要测试app的入口页面，获取命令：aapt dump badging apk路径，查看launchable-activity: name='
                "noReset": True,  # 在此会话之前，请勿重置应用程序状态
                }

            self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

        else:
            self.driver.launch_app()


        self.driver.implicitly_wait(30)

        return self

    def restart(self):

        self.driver.close_app()
        self.driver.launch_app()

    def stop(self):
        self.driver.quit()

    def goto_main(self):
        return Main(self.driver)