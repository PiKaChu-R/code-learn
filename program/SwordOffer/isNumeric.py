#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
    @File    :   isNumeric.py
    @Time    :   2019/09/15 15:54:47
    @Author  :   R.
    @Version :   1.0
    @Contact :   827710637@qq.com
    @Desc    :   None
'''

'''
    请实现一个函数用来判断字符串是否表示数值（包括整数和小数）。
    例如，字符串"+100","5e2","-123","3.1416"和"-1E-16"都表示数值。
    但是"12e","1a3.14","1.2.3","+-5"和"12e+4.3"都不是。
'''


# here put the import lib
class Solution:
    def isNumeric(self, s):
        if not s:
            return False

        flag_num = False
        flag_e = False
        flag_p = False

        for index,val in enumerate(s):
            if val in ['+','-']:
                if index > 0 and (s[index-1] != 'e' and s[index-1] != 'E'):
                    return False
            elif val.isdigit():
                flag_num = True
            elif val == '.':
                if flag_p or flag_e:
                    return False
                flag_p = True
            elif val == 'e' or val == 'E':
                if not flag_e and flag_num:
                    flag_e = True
                    flag_num = False
                else:
                    return False
            else:
                return False
        if flag_e and not flag_num:
            return False
        return True
    
    # Python Trick
    def isNumeric2(self,s):
        try:
            float(s)
            if s[0:2] != '+-' and s[0:2] != '-+':
                return True
            else:
                return False
        except:
            return False