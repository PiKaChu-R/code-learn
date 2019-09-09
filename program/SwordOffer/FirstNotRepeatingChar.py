#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
    @File    :   FirstNotRepeatingChar.py
    @Time    :   2019/09/09 15:48:34
    @Author  :   R.
    @Version :   1.0
    @Contact :   827710637@qq.com
    @Desc    :   None
'''

'''
    在一个字符串(1<=字符串长度<=10000，全部由大写字母组成)
    中找到第一个只出现一次的字符。
'''


# here put the import lib
def FirstNotRepeatingChar(s):
    if not s or len(s) <= 0:
        return -1 
    
    for i in range(len(s)):
        if s.find(s[i]) == s.rfind(s[i]):
            return i
    return -1

# s = Solution()
print(FirstNotRepeatingChar('abaccdeff'))