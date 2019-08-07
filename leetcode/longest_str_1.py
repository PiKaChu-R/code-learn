#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
    @File    :   longest_str_1.py
    @Time    :   2019/06/14 19:47:23
    @Author  :   R.
    @Version :   1.0
    @Contact :   827710637@qq.com
    @Desc    :   采用了中心扩散的方法，还可以采用Manacher算法（Python未实现）
'''

'''
给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为 1000。

输入: "babad"
输出: "bab"
注意: "aba" 也是一个有效答案。
'''


# here put the import lib

class Solution:
    def longestPalindrome(self,s):
        
        size = len(s)
        if size == 0:
            return ''
        
        longest_palindrome = 1
        longest_palindrome_str = s[0]

        for i in range(size):
            palindrome_odd,odd_len = self.__center_spread(s,size,i,i)
            palindrome_new,new_len = self.__center_spread(s,size,i,i+1)

            cur_max_sub = palindrome_odd if odd_len >= new_len else palindrome_new

            if len(cur_max_sub) > longest_palindrome:
                longest_palindrome = len(cur_max_sub)
                longest_palindrome_str = cur_max_sub
            
        return longest_palindrome_str

    def __center_spread(self, s,size,left,right):
        l = left
        r = right

        while l >= 0 and r <size and s[l]==s[r]:
            l -= 1
            r += 1
        return  s[l+1:r],r-l-1

if __name__ == "__main__":
    s = input()
    so = Solution()
    k = so.longestPalindrome(s)
    print (k)