#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
    @File    :   word-extract.py
    @Time    :   2019/04/16 17:00:01
    @Author  :   R.
    @Version :   1.0
    @Contact :   827710637@qq.com
    @Desc    :   None
'''
''' 
    【问题描述】给定一个段落，由 N 个句子组成。第 i 个句子的长度为 L[i]，包含的单词个数为 W[i]。
句子不包含任何除字母和空格( ) 外的符号。每个句子内部，含有若干个单词，由空格( ) 分隔。句子不会包含连续的空格。
随后给定 M 个查询，每个查询包含一个句子，需要在段落中寻找相同单词数量最多的句子。重复的单词只计一次，且不区分大小写。
输入数据将保证结果是存在且唯一的。
'''
# here put the import lib

NM = input().strip().split()
N, M = map(int, NM)

list_word = []

for i in range(N+M):
    list_word.append(input())

list1 = []
for i in list_word:
    list1.append(i.strip().split())

# print list1

count = 0
list3 = []
for i in range(N, N+M):
    list2 = []
    for k in range(N):
        for j in list1[i]:
            if j in list1[k]:
                count += 1
        list2.append(count)
        count = 0
    list3.append(list2)

for i in range(len(list3)):
    indexi = list3[i].index(max(list3[i]))
    print (indexi)
    print (list_word[indexi])
