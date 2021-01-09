# -*- coding: utf-8 -*-
# @Time     :  2021/1/9 14:45
# @Author   :  zhangyuxin
# @Email    :  zhangyuxin.aikebo@bytedance.com
# @File     :  test_demo.py

def a(fun):

    print("a")
    def aa(*args,**kwargs):
        print("aa1")
        fun(*args,**kwargs)
        print("aa2")
    return aa


def b(fun):
    print("b")
    def bb(*args, **kwargs):
        print("bb1")
        fun(*args, **kwargs)
        print("bb2")

    return bb

@b
@a
def test_c():
    print("cc")



# 执行顺序 内部函数外部由离函数最近的执行，  内部函数内部由最远的开始执行

