#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
    @File    :   Hcf_lcd.py
    @Time    :   2019/04/25 15:21:52
    @Author  :   R.
    @Version :   1.0
    @Contact :   827710637@qq.com
    @Desc    :   None
'''

'''
    分别编写求两个整数的最大公约数的函数hcf和求最小公倍数的函数lcd。主函数已给出，
    其从键盘接收两个整数，调用这两个函数后输出结果。
    （提示：求最大公约数可用辗转相除法。即将大数作为被除数，小数作为除数，若二者
    余数不为0，则将小数作为被除数，余数作为除数，…直到余数为0。求最小公倍数则用
    两数的积除以最大公约数即可。）
'''


# here put the import lib

def hcf(u,v):
    if v>u:
        u,v=v,u
    r=u%v
    while r!=0:
        u=v
        v=r
        r=u%v
    return v
  
def lcd(u,v,h):
    return u*v/h
  
u=int(input("请输入第一个整数："))
v=int(input("请输入第二个整数："))
h=hcf(u,v)
print("%d和%d的最大公约数为%d："%(u,v,h))
l=lcd(u,v,h)
print("%d和%d的最小公倍数为%d："%(u,v,l))
