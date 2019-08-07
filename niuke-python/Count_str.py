#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
    @File    :   Count_str.py
    @Time    :   2019/04/25 14:54:42
    @Author  :   R.
    @Version :   1.0
    @Contact :   827710637@qq.com
    @Desc    :   None
'''

'''
    编写函数，接收一个字符串，分别统计大写字母、小写字母、数字、其他字符的个数，
    并以元组的形式返回结果。
'''


# here put the import lib


def count(word):

    count_all = [0, 0, 0, 0]
    for i in word:
        if i.islower():
            count_all[0] += 1
        elif i.isupper():
            count_all[1] += 1
        elif i.isdigit():
            count_all[2] += 1
        else:
            count_all[3] += 1
    print ((count_all[0],count_all[1],count_all[2],count_all[3]))

if __name__ == "__main__":
    str_word = input()
    count(str_word)
