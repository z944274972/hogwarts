# -*- coding: utf-8 -*-
# @Time     :  2021/1/10 16:55
# @Author   :  zhangyuxin
# @Email    :  zhangyuxin.aikebo@bytedance.com
# @File     :  conftest.py
import os
import signal
import subprocess

import pytest


# 针对移动设备，不适用web页面
# @pytest.fixture(scope="module",autouse=True)
@pytest.fixture(scope="module")
def record_vedio():

    cmd = "scrcpy --record file.mp4"
    p = subprocess.Popen(cmd,shell= True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
    yield
    os.kill(p.pid,signal.CTRL_C_EVENT)