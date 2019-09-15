#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
    @File    :   match.py
    @Time    :   2019/09/15 15:47:47
    @Author  :   R.
    @Version :   1.0
    @Contact :   827710637@qq.com
    @Desc    :   None
'''

'''
    请实现一个函数用来匹配包括'.'和'*'的正则表达式。
    模式中的字符'.'表示任意一个字符，而'*'表示它前面的字符可以出现任意次（包含0次）。
    在本题中，匹配是指字符串的所有字符匹配整个模式。
    例如，字符串"aaa"与模式"a.a"和"ab*ac*a"匹配，但是与"aa.a"和"ab*a"均不匹配
'''


# here put the import lib
class Solution:
    def match(self,s,pattern):
        if not s or not pattern:
            return False
        
        if s == pattern:
            return True
        
        flag = bool(s) and pattern[0] in [s[0],'.']

        if len(pattern) >= 2 and pattern[1] == '*':
            return (self.match(s,pattern[2:])) or (flag and self.match(s[1:],pattern))
        else:
            return flag and self.match(s[1:],pattern[1:])

s = Solution()
print(s.match('aaa', ''))