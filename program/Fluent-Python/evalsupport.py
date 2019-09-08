#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
    @File    :   evalsupport.py
    @Time    :   2019/09/06 11:57:06
    @Author  :   R.
    @Version :   1.0
    @Contact :   827710637@qq.com
    @Desc    :   None
'''

'''
    evaltime.py 的支持程序
'''


# here put the import lib
print('<[100]> evalsupport module start')


def deco_alpha(cls):
    print('<[200]> deco_alpha')

    def inner_1(self):
        print('<[300]> deco_alpha:inner_1')
    cls.method_y = inner_1
    return cls


class MetaAleph(type):
    print('<[400]> MetaAleph body')

    def __init__(cls, name, bases, dic):
        print('<[500]> MetaAleph.__init__')

        def inner_2(self):
            print('<[600]> MetaAleph.__init__:inner_2')
        cls.method_z = inner_2


print('<[700]> evalsupport module end')
