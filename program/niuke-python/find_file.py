#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
    @File    :   find_file.py
    @Time    :   2019/04/25 14:48:20
    @Author  :   R.
    @Version :   1.0
    @Contact :   827710637@qq.com
    @Desc    :   None
'''

'''
    编写程序，用户输入一个目录和一个文件名，搜索该目录及其子目录中是否存在该文件。
'''


# here put the import lib

import sys
import os


def File_find(path, name):

    paths = os.walk(path)
    for root, dirs, files in paths:
        if name in files:
            print ('Find.') 
            break
    

if __name__ == "__main__":

    fl_path = input("Path:")
    fl_name = input("Name:")

    File_find(fl_path, fl_name)
