#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
    @File    :   13-RomanToInt.py
    @Time    :   2019/08/27 17:25:48
    @Author  :   R.
    @Version :   1.0
    @Contact :   827710637@qq.com
    @Desc    :   None
'''

'''
    内容同12题相似，转换顺序变反。
'''


# here put the import lib

class Solution:
    def romanToInt(self, s):
        # 将所有的情况，基础加特殊，构建一个字典，对字符串进行遍历。
        dic =  {'M':1000, 'CM': 900, 'D': 500, 'CD': 400, 
                'C':100, 'XC':90, 'L':50, 'XL':40,
                'X':10, 'IX': 9, 'V':5, 'IV':4,
                'I':1}
        i =0
        res = 0
        while i < len(s):
            # 对当前位置的下一位置进行判断-判断当前位置和下一位置是否在字典中。
            if i+1 < len(s) and s[i] + s[i+1] in dic:
                res += dic[s[i] + s[i+1]]
                # 因为一次处理两个字符，所以i+2
                i += 2
            elif s[i] in dic:
                res += dic[s[i]]
                i += 1
        return res

so = Solution()
k = so.romanToInt('MCMXCIV')
print(k)