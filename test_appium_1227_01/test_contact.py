# -*- coding: utf-8 -*-
# @Time     :  2020/12/27 14:17
# @Author   :  zhangyuxin
# @Email    :  zhangyuxin.aikebo@bytedance.com
# @File     :  test_contact.py

from time import sleep

from appium import webdriver
import pytest
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.wait import WebDriverWait


class TestContact:

    def setup(self):

        desired_caps = {
            # "automationName": "UiAutomator2",  # 使用哪个自动化引擎,appium1.x可以不用写
            "platformName": "Android",  # 使用哪个移动操作系统平台
            "platformVersion": '6.0.1',  # 移动操作系统版本
            "deviceName": "127.0.0.1:7555",  # 使用的移动设备或模拟器的种类,需要在cmd命令下，敲adb devices查看
            "appPackage": "com.tencent.wework",  # 所要测试的app的包名，获取命令：aapt dump badging apk路径，查看package: name=
            "appActivity": ".launch.LaunchSplashActivity",
            # 所要测试app的入口页面，获取命令：aapt dump badging apk路径，查看launchable-activity: name='
            "noReset": True,  # 在此会话之前，请勿重置应用程序状态
            "settings[waitForIdleTimeout]":0 }

        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        self.driver.implicitly_wait(30)


    def teardown(self):
        self.driver.quit()


    def test_contact(self):

        self.driver.find_element(MobileBy.XPATH,'//*[@resource-id="com.tencent.wework:id/elq" and @text="通讯录"]').click()
        self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,'new UiScrollable(new UiSelector().scrollable(true).instance(0)).scrollIntoView(new UiSelector().text("添加成员").instance(0));').click()
        self.driver.find_element(MobileBy.XPATH,"//*[@text='手动输入添加']").click()
        self.driver.find_element(MobileBy.XPATH,'//*[contains(@text,"姓名")]/..//*[@text="必填"]').send_keys("小虎牙")
        self.driver.find_element(MobileBy.XPATH,'//*[contains(@text,"性别")]/..//*[@text="男"]').click()
        def wait_ele_for(driver:webdriver):
            ele = driver.find_elements(MobileBy.XPATH,'//*[@text="女"]')
            return len(ele)>0
        WebDriverWait(self.driver,10).until(wait_ele_for)
        self.driver.find_element(MobileBy.XPATH,'//*[@text="女"]').click()
        self.driver.find_element(MobileBy.XPATH,'//*[contains(@text,"手机")]/..//*[@text="手机号"]').send_keys("18212345678")
        self.driver.find_element(MobileBy.XPATH, '//*[@text="保存"]').click()


if __name__ == '__main__':
    pytest.main()