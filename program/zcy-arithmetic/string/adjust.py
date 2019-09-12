#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
    @File    :   adjust.py
    @Time    :   2019/09/12 20:44:20
    @Author  :   R.
    @Version :   1.0
    @Contact :   827710637@qq.com
    @Desc    :   None
'''

'''
    字符串的调整与替换
    补充问题：字符串只有数字和*，将*放在字符串首部(时间O(n)，空间O(1))
'''


# here put the import lib
# 时间复杂度O(n)，空间复杂度O(1)
# python中没有字符串数组，不知道怎么是空间复杂度为O(1)的情况
def adjust(s):
    if not s :
        return
    ans = ''
    for i in range(len(s)):
        if s[i] == ' ':
            ans += '%20'
        else:
            ans += s[i]
    return ans
