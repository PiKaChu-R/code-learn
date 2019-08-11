#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
    @File    :   str_no_repeat.py
    @Time    :   2019/06/10 20:02:49
    @Author  :   R.
    @Version :   1.0
    @Contact :   827710637@qq.com
    @Desc    :   None
'''

'''
给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。
输入: "abcabcbb"
输出: 3 
'''


# here put the import lib

def lengthOfLongestSubstring(s):
    if not s:
        return 0
    left = 0
    Sliding_Window = set()
    max_len = 0
    cur_len = 0
    for i in range(len(s)):
        cur_len += 1
        while s[i] in Sliding_Window:
            Sliding_Window.remove(s[left])
            left += 1
            cur_len -= 1
        if cur_len > max_len:
            max_len = cur_len
        Sliding_Window.add(s[i])
    return max_len

def lengthOfLongestSubstring2(s):
    i = 0
    res = 0
    for j in range(len(s)):
        if s[j] not in s[i:j]:
            res = max(res,j+1-i)
        else:
            i += s[i:j].index(s[j])+1
    return res


if __name__ == "__main__":
    s = 'pwwkew'
    k = lengthOfLongestSubstring2(s)
    print(k)
