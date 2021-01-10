# -*- coding: utf-8 -*-
# @Time     :  2021/1/9 14:29
# @Author   :  zhangyuxin
# @Email    :  zhangyuxin.aikebo@bytedance.com
# @File     :  black_handle.py
import logging

import allure

logging.basicConfig(level=logging.INFO)

def black_wrapper(fun):

    def run(*args,**kwargs):
        base = args[0]


        try:
            logging.info("start find : \nargs :" + str(args) + "kwargs :" + str(kwargs))
            return fun(*args,**kwargs)

        except Exception as e:

            base.screen_shot("tmp.png")
            with open("./tmp.png",'rb') as f:
                picture_data = f.read()
            allure.attach(picture_data,attachment_type=allure.attachment_type.PNG)
            for i in base.black_list:
                ele = base.finds(*i)
                if len(ele) > 0:
                    ele[0].click()
                    return fun(*args,**kwargs)
            raise e
    return run