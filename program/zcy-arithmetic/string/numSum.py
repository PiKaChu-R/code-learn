#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
    @File    :   numSum.py
    @Time    :   2019/09/05 17:53:16
    @Author  :   R.
    @Version :   1.0
    @Contact :   827710637@qq.com
    @Desc    :   None
'''

'''
    字符串中数字子串的和，判断负数，判断大于10的数字。
'''


# here put the import lib
# 时间O(n)，空间O(1)

def numSum(s):
    if s == None:
        return 0

    res = 0
    num = 0
    posi = True
    cur = 0
    for i in range(len(s)):
        cur = s[i] 
        if cur < '0' or cur > '9':
            res += num
            num = 0
            if s[i] == '-':
                if i-1 > -1 and s[i-1] == '-':
                    posi = not posi
                else:
                    posi = False
            else:
                posi = True
        else:
            if posi:
                num = num * 10 + int(cur)
            else:
                num = num * 10 - int(cur)
    res += num
    return res

print(numSum('A-1b--2v--d6e'))
print(numSum('A1cd2e33'))