# -*- coding: utf-8 -*-
# @Time     :  2020/12/27 20:00
# @Author   :  zhangyuxin
# @Email    :  zhangyuxin.aikebo@bytedance.com
# @File     :  base_page.py
import yaml
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from test_frame_0110_02.black_handle import black_wrapper


class BasePage:

    FIND = 'find'
    ACTION = 'action'
    FIND_CLICK = 'find_click'
    TYPE = 'type'
    SEND = 'send'
    CONTENT = 'data'

    def __init__(self):

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

        self.driver.implicitly_wait(30)

        self.black_list = [(By.XPATH,'//*[@resource-id="com.xueqiu.android:id/iv_close"]')]

    @black_wrapper
    def find(self,by,locator):

            return self.driver.find_element(by,locator)

    def finds(self,by,locator):

        return self.driver.find_elements(by,locator)

    def find_click(self,by,locator):

        return self.find(by,locator).click()

    def scroll_find(self,text):

        return self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,f'new UiScrollable(new UiSelector().scrollable(true).instance(0)).scrollIntoView(new UiSelector().text("{text}").instance(0));')

    def scroll_find_click(self,text):

        return self.scroll_find(text).click()

    def swip_find(self,by,locator):

        eles = self.finds(by,locator)
        while len(eles) == 0:
            self.driver.swipe(0,600,0,400)
            eles = self.finds(by,locator)
        self.driver.implicitly_wait(10)
        return eles[0]

    def swip_find_click(self,by,locator):
        self.swip_find(by,locator).click()

    def find_sendkeys(self,by,locator,text):

        return self.find(by,locator).send_keys(text)

    def wait_for(self,by,locator):
        def wait(driver:WebDriver):
            eles = driver.find_elements(by,locator)
            return len(eles)>0
        WebDriverWait(self.driver, 10).until(wait)


    def get_toast_text(self):

        return self.find(MobileBy.XPATH,'//*[@class="android.widget.toast"]').click()


    def load(self,yaml_path):

        global me
        with open(yaml_path,'r',encoding='utf-8') as f:
            data = yaml.load(f)
        for step in data:
            expr = step.get(self.FIND)
            method = step.get(self.TYPE)
            if method == "xpath":
                me = By.XPATH
            action = step.get(self.ACTION)
            if action == self.FIND_CLICK:
                self.find_click(me, expr)
            elif action == self.SEND:
                content = step.get(self.CONTENT)
                self.find_sendkeys(me,expr,content)

    def screen_shot(self,picture_shot):

        self.driver.save_screenshot(picture_shot)
