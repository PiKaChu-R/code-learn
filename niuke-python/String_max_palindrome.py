#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
    @File    :   String_max_palindrome.py
    @Time    :   2019/04/17 17:01:56
    @Author  :   R.
    @Version :   1.0
    @Contact :   827710637@qq.com
    @Desc    :   None
'''

'''
    求一个字符串的最大回文前缀长度。回文是指正反方向读起来都一样的字符串，比如“abcdcba”就是一个回文。
    输入
    一个文本文件，至少包含一个字节。每个字节是一个字符。最大长度可能有几十万字节。
    输出
    最大回文前缀的长度。
    样例输入
    Sogou
    样例输出
    1
    注意本题是求回文前缀的长度，需要从字符串的首部开始，字符串中间到尾部的部分形成的回文不算。
'''
''' 
    math.ceil():向上取整
    math.floor():向下取整
    四舍五入：round()
'''

# here put the import lib
import math

def max_palindrome(s):
    max_s = 0
    for i in range(math.ceil(len(s)/2)):
        n = len(s)-i-1
        if (i!=n) and (i+n<len(s)):
            if s[i] == s[n]:
                max_s +=2
            else:
                # max_s += 1
                break
    max_s += 1
    print (max_s)


if __name__ == "__main__":
    str_list = input("Input the string:")
    max_palindrome(str_list)