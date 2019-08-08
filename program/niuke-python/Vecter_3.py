#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
    @File    :   Vecter_3.py
    @Time    :   2019/04/19 17:28:04
    @Author  :   R.
    @Version :   1.0
    @Contact :   827710637@qq.com
    @Desc    :   None
'''

'''
    设计一个三维向量类，并实现向量的加法、减法以及向量与标量的乘法和除法运算。
'''


# here put the import lib

class Vecter3:
    def __init__(self, x=0,y=0,z=0):
        self.X = x
        self.Y = y
        self.Z = z
    def __add__(self,n):
        r = Vecter3()
        r.X = self.X +n.X
        r.Y = self.Y +n.Y
        r.Z = self.Z +n.Z
        return r
    def __sub__(self,n):
        r = Vecter3()
        r.X = self.X -n.X
        r.Y = self.Y -n.Y
        r.Z = self.Z -n.Z
        return r
    def __mul__(self,n):
        r = Vecter3()
        r.X = self.X *n
        r.Y = self.Y *n
        r.Z = self.Z *n
        return r
    def __div__(self,n):
        r = Vecter3()
        r.X = self.X /n
        r.Y = self.Y /n
        r.Z = self.Z /n
        return r
    def __floordiv__(self,n):
        r = Vecter3()
        r.X = self.X //n
        r.Y = self.Y //n
        r.Z = self.Z //n
        return r
    def show(self):
        print((self.X,self.Y,self.Z))

if __name__ == "__main__":
    v1 = Vecter3(1,2,3)
    v2 = Vecter3(4,5,6)
    v3 = v1+v2
    v3.show()
    v4 = v1-v2
    v4.show()
    v5 = v1*3
    v5.show()
    v6 = v1//2.0
    v6.show()