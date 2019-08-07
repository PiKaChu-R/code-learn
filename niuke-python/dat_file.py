#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
    @File    :   dat_file.py
    @Time    :   2019/04/22 19:38:25
    @Author  :   R.
    @Version :   1.0
    @Contact :   827710637@qq.com
    @Desc    :   pickle:存入后再读取会出现问题 Ran out of input
'''

'''
    编写程序，将包含学生成绩的字典保存为二进制文件，然后再读取内容并显示。
'''


# here put the import lib
import pickle

# d = {'张三': 98, '李四': 90, '王五': 100}
# # print(d)
# f = open(r'D:\myproject\score.dat', 'wb')
# pickle.dump(1, f)
# pickle.dump(d, f)
# f.close

f = open(r'D:\myproject\score.dat', 'rb')
pickle.load(f)
d = pickle.load(f)
f.close()
print(d)
