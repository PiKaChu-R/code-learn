#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
    @File    :   StrToInt.py
    @Time    :   2019/09/09 17:38:42
    @Author  :   R.
    @Version :   1.0
    @Contact :   827710637@qq.com
    @Desc    :   None
'''

'''
    将一个字符串转换成一个整数，要求不能使用字符串转换整数的库函数
'''


# here put the import lib
def StrToInt(s):
    if not s:
        return 0
    n = len(s)
    ans = ''
    flag = 1
    for i in range(n):
        if s[i] in ['+','-'] and i == 0:
            if s[i] == '-':
                flag = 0
        elif '0' <= s[i] <= '9':
            ans += s[i]
        else:
            return 0
    if ans:
        if flag == 1:
            return int(ans)
        else:
            return -int(ans)
    else:
        return 0