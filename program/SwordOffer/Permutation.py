#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
    @File    :   Permutation.py
    @Time    :   2019/09/09 14:33:45
    @Author  :   R.
    @Version :   1.0
    @Contact :   827710637@qq.com
    @Desc    :   None
'''

'''
    输入一个字符串,按字典序打印出该字符串中字符的所有排列。例如输入字符串abc,
    则打印出由字符a,b,c所能排列出来的所有字符串abc,acb,bac,bca,cab和cba。
    输入一个字符串,长度不超过9(可能有字符重复),字符只包括大小写字母。
'''


# here put the import lib
def Permutation(ss):
    if not ss:
        return []

    res = []
    n = len(ss)
    visited = [0] * n
    s = sorted(ss)

    def backtrack(s, tmp, length):
        if length == n:
            res.append(tmp)
            return
        for i in range(n):
            if visited[i] or (i > 0 and s[i] == s[i-1] and not visited[i-1]):
                continue
            visited[i] = 1
            backtrack(s, tmp+s[i], length+1)
            visited[i] = 0
    backtrack(s, '', 0)
    return res

def Permutation2(ss):
    if not ss :
        return []
    
    res = []
    n = len(ss)
    def backtrack(s,tmp,length):
        if length == n:
            res.append(tmp)
            return 
        for i in range(len(s)):
            backtrack(s[:i]+s[i+1:],tmp+s[i],length+1)
        

    backtrack(ss,'',0)
    return res

class Solution:
    def Permutation(self, ss):
        # write code here
        if not len(ss):
            return []
        if len(ss) == 1:
            return list(ss)

        charList = list(ss)
        charList.sort()
        pStr = []
        for i in range(len(charList)):
            if i > 0 and charList[i] == charList[i-1]:
                continue
            temp = self.Permutation(''.join(charList[:i])+''.join(charList[i+1:]))
            for j in temp:
                pStr.append(charList[i]+j)
        return pStr


ss = 'acb'
S = Solution()
print(S.Permutation(ss))
# print(group(ss))
