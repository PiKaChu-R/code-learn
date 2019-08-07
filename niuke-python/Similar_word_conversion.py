#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
    @File    :   Similar_word_conversion.py
    @Time    :   2019/04/18 17:32:08
    @Author  :   R.
    @Version :   1.0
    @Contact :   827710637@qq.com
    @Desc    :   None
'''

'''
    see和seek、cat和cut等，现在提供3种编辑操作：insert、remove、replace，
    通过在单词1上进行这些操作，可以让单词1变成单词2.
    说明：
        1）3种编辑操作的代价是一样的
        2）并且每次只能操作一个字符串的一个字母
        3）只需要考虑在字符串1上进行编辑操作即可
    输入
    输入一行，有两个字符串，以空格分隔。
    输出
    输出为最小编辑次数。
    样例输入
    geek gesek
    样例输出
    1
'''


# here put the import lib

def opera_count(str_ls):
    if len(str_ls[0]) == len(str_ls[1]):
        result = sam_len(str_ls)
    elif len(str_ls[0]) < len(str_ls[1]):
        result = diff_len(str_ls)
    else:
        temp = str_ls[0]
        str_ls[0] = str_ls[1]
        str_ls[1] = temp
        result = diff_len(str_ls)
        

    print (result)

def sam_len(str_ls):
    count = 0
    for i in range(len(str_ls[0])):
        if str_ls[0][i] != str_ls[1][i]:
            count += 1
    return count

def diff_len(str_ls):
    str_list_1 = list(str_ls[0])
    str_list_2 = list(str_ls[1])
    
    # count = 0
    for i in range(len(str_list_1)):
        if str_list_1[i] in str_list_2:
            # k = str_list_1[i]
            # str_list_1.remove(k)
            str_list_2.remove(str_list_1[i])

    return len(str_list_2)


if __name__ == "__main__":
    str_list = input().strip().split()
    opera_count(str_list)
