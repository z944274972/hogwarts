# -*- coding: utf-8 -*-
# @Time     :  2020/12/17 20:57
# @Author   :  zhangyuxin
# @Email    :  zhangyuxin.aikebo@bytedance.com
# @File     :  test_fuyong.py
import time

import pytest
import yaml
from selenium import webdriver

class TestFuyong:

    def setup(self):
        pass

    def teardown(self):
        pass

    # 复用浏览器操作
    def test_fuyong(self):
        opt = webdriver.ChromeOptions()
        opt.debugger_address="127.0.0.1:9222"
        driver = webdriver.Chrome(options=opt)
        driver.get("https://work.weixin.qq.com/wework_admin/frame")
        print(driver.get_cookies())


    # cookies为上述生成自己复制所得
    def test_cookie(self):
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get("https://work.weixin.qq.com/wework_admin/loginpage_wx?redirect_uri=https://work.weixin.qq.com/wework_admin/frame")
        cookies = [{'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.vid', 'path': '/', 'secure': False, 'value': '1688853331098495'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.vst', 'path': '/', 'secure': False, 'value': 'aTLIE_w52Jggnrpf3JOFVgB9YAhpQGxoW5I-JCGoCMm2gqtWxcJcojRfa_wI_f0I0YpH9fGN6RKWxZKBHHIPXdaclBmxJsSFhBJTRtU92ZZhuM-kQ81HFu0yHPmOwPMAmScUu4GhBme9JKzO1yIP6WWp_aGa83bA56puLzgpRsKq389g5SfPWBUFGZECvcKGajCGFW0LYn3ITrpbk8YJuXPlK-vwBsxSaBv3KCPD-lBnBUzA7_rBuZyc1MiylGBtF0avEGTPQG1CUHNeVO8vog'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.vid', 'path': '/', 'secure': False, 'value': '1688853331098495'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.corpid', 'path': '/', 'secure': False, 'value': '1970324946208804'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ref', 'path': '/', 'secure': False, 'value': 'direct'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ltype', 'path': '/', 'secure': False, 'value': '1'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.d2st', 'path': '/', 'secure': False, 'value': 'a2971999'}, {'domain': 'work.weixin.qq.com', 'expiry': 1608243704, 'httpOnly': True, 'name': 'ww_rtkey', 'path': '/', 'secure': False, 'value': '4dgb8a8'}, {'domain': '.qq.com', 'expiry': 1608298588, 'httpOnly': False, 'name': '_gid', 'path': '/', 'secure': False, 'value': 'GA1.2.1117472406.1608212169'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.refid', 'path': '/', 'secure': False, 'value': '02137474'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.sid', 'path': '/', 'secure': False, 'value': 'ix8Fvd9fFacYROxB21EBsoG-6MioPB6s1xIyVi888mFVWnJUbtaRHwJUNmILeakq'}, {'domain': '.qq.com', 'expiry': 1608212229, 'httpOnly': False, 'name': '_gat', 'path': '/', 'secure': False, 'value': '1'}, {'domain': '.qq.com', 'expiry': 1671284188, 'httpOnly': False, 'name': '_ga', 'path': '/', 'secure': False, 'value': 'GA1.2.2082642422.1608212169'}, {'domain': '.work.weixin.qq.com', 'expiry': 1639748168, 'httpOnly': False, 'name': 'wwrtx.c_gdpr', 'path': '/', 'secure': False, 'value': '0'}, {'domain': '.work.weixin.qq.com', 'expiry': 1610804210, 'httpOnly': False, 'name': 'wwrtx.i18n_lan', 'path': '/', 'secure': False, 'value': 'zh'}]
        for cookie in cookies:
            driver.add_cookie(cookie)
        driver.get("https://work.weixin.qq.com/wework_admin/frame")
        driver.quit()

    # 获取cookie，序列化后存入yaml文件内cookie.yml
    def test_write_yaml(self):
        opt = webdriver.ChromeOptions()
        opt.debugger_address = "127.0.0.1:9222"
        driver = webdriver.Chrome(options=opt)
        driver.implicitly_wait(5)
        driver.get("https://work.weixin.qq.com/wework_admin/frame#contacts")
        time.sleep(10)
        cookie = driver.get_cookies()
        print(cookie)
        with open("./cookie.yml","w",encoding="utf-8") as f:
            yaml.dump(cookie,f)

    # 使用序列化cookie的方法进行登录
    def test_login(self):
        driver = webdriver.Chrome()
        driver.implicitly_wait(5)
        driver.get("https://work.weixin.qq.com/wework_admin/loginpage_wx?")
        with open("cookie.yml", encoding="UTF-8") as f:
            yaml_data = yaml.safe_load(f)
            for cookie in yaml_data:
                if "expiry" in cookie.keys():
                    del cookie["expiry"]
                driver.add_cookie(cookie)
        driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
        time.sleep(10)



