# -*- coding: utf-8 -*-
# @Time     :  2021/1/9 14:29
# @Author   :  zhangyuxin
# @Email    :  zhangyuxin.aikebo@bytedance.com
# @File     :  black_handle.py

def black_wrapper(fun):

    def run(*args,**kwargs):
        base = args[0]

        try:
            return fun(*args,**kwargs)

        except Exception as e:

            for i in base.black_list:
                ele = base.finds(*i)
                if len(ele) > 0:
                    ele[0].click()
                    return fun(*args,**kwargs)
            raise e
    return run