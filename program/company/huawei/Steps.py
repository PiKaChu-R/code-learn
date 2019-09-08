#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
    @File    :   Steps.py
    @Time    :   2019/09/08 21:46:25
    @Author  :   R.
    @Version :   1.0
    @Contact :   827710637@qq.com
    @Desc    :   None
'''

'''
    走台阶
'''


# here put the import lib
def solution(n):
    if n == 0 :
        return 0
    if n == 1 or n == 2:
        return n
    
    a = 1
    b = 1

    for _ in range(2,n+1):
        a,b = a+b,a

    return b

print(solution(10))