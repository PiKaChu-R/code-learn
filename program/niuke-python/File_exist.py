#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
    @File    :   File_exist.py
    @Time    :   2019/04/19 16:00:05
    @Author  :   R.
    @Version :   1.0
    @Contact :   827710637@qq.com
    @Desc    :   None
'''

'''
        请输入一个文件路径名或文件名，查看该文件是否存在，如存在，打开文件并在屏幕上输
    出该文件内容；如不存在，显示“输入的文件未找到！ ” 并要求重新输入；如文件存在但
    在读文件过程中发生异常，则显示“文件无法正常读出！”并要求重新输入。
    （提示：请使用异常处理。“文件未找到”对应的异常名为：FileNotFoundError，其他异常直接
    用except匹配）
'''


# here put the import lib

import os

while True:
    try:
        filename = input('请输入文件路径名或文件名：')
        f = open(filename.strip())
        print(f.read())
    except FileNotFoundError:
        print("输入的文件未找到！")
    except:
        print("文件无法正常读出！")
    else:
        break
f.close()
