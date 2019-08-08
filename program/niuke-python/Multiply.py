#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
    @File    :   multiply.py
    @Time    :   2019/04/16 15:45:23
    @Author  :   R.
    @Version :   1.0
    @Contact :   827710637@qq.com
    @Desc    :   None
'''
''' 
    TODO:实现两个函数能够同时在一个里面实现，通过一个调用实现两种形式
         问题：参数问题。
'''
# here put the import lib
import sys
import math

# def multiply(x,y):
#     return x*y

def multiply(x):
    # print (x)
    def multiplyx(y):
        return x*y
    return multiplyx

if __name__ == "__main__":
    # k = multiply(1,2)
    h = multiply(1)(2)
    print(h)