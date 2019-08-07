#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
    @File    :   English_learn.py
    @Time    :   2019/04/19 16:02:55
    @Author  :   R.
    @Version :   1.0
    @Contact :   827710637@qq.com
    @Desc    :   程序存在问题
'''

'''
        小王希望用电脑记录他每天掌握的英文单词。请设计程序和相应的数据结构，使
    小王能记录新学的英文单词和其中文翻译，并能很方便地根据英文来查找中文。
    （参考：数据结构建议用集合。集合添加：dic[key]=value 判断key是否在集合中：
    if key in dic)。
'''


# here put the import lib
import os
import csv


def add_dic(dic_word):
    while True:
        word = input("请输入英文单词（直接按回车结束）：")
        if len(word) == 0:
            break
        mean_chinese = input("请输入中文翻译：")
        dic_word[word] = mean_chinese
        print("该单词已添加到字典库。")


def search_dic(dic_word):
    while True:
        word = input("请输入要查询的英文单词（直接按回车结束）：")
        if len(word) == 0:
            break
        if word in dic_word:
            print("%s的中文翻译是%s" % (word, dic_word[word]))
        else:
            print("字典库中未找到这个单词")


if __name__ == "__main__":

    csvFile_name = "D:/myproject/data/English.csv"
    
    if not os.path.exists(csvFile_name):
        os.makedirs(csvFile_name)

    csvFile = open(csvFile_name, "r+")

    for line in csvFile:
        print (line)

    worddic = dict()
    while True:
        print("请选择功能：\n1:输入\n2：查找\n3：退出")
        c = input()
        if c == "1":
            add_dic(worddic)
        elif c == "2":
            search_dic(worddic)
        elif c == "3":
            break
        else:
            print("输入有误！")
