#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
    @File    :   Z_change.py
    @Time    :   2019/06/14 20:01:12
    @Author  :   R.
    @Version :   1.0
    @Contact :   827710637@qq.com
    @Desc    :   None
'''

'''
将一个给定字符串根据给定的行数，以从上往下、从左到右进行 Z 字形排列。

比如输入字符串为 "LEETCODEISHIRING" 行数为 3 时，排列如下：
L   C   I   R
E T O E S I I G
E   D   H   N

输入: s = "LEETCODEISHIRING", numRows = 4
输出: "LDREOEIIECIHNTSG"
解释:
L     D     R
E   O E   I I
E C   I H   N
T     S     G

'''


# here put the import lib

s = 'LEETCODEISHIRING'

n = len(s)
numRows = 3
data = []
distance = numRows*2-2
for i in range(0,n,distance):
    data.append(s[i:i+distance])

print (data)
res= ''
for i in range(numRows):
    for tmp in data:
        if i <len(tmp):
            if i==0 or i==numRows-1:
                res += tmp[i]
            else:
                res+=tmp[i]
                if distance-i<len(tmp):
                    res += tmp[distance-i]

print(res)
# print (list_1)