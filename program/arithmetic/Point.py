#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
    @File    :   Point.py
    @Time    :   2019/06/21 11:36:40
    @Author  :   R.
    @Version :   1.0
    @Contact :   827710637@qq.com
    @Desc    :   最近点对问题，分治
'''

'''
'''


# here put the import lib
from math import sqrt

# 蛮力法
def solve(points):
    n = len(points)
    min_d = float("inf") # 最小距离：无穷大
    min_ps = None        # 最近点对
    for i in range(n-1):
        for j in range(i+1, n):
            d = sqrt((points[i][0] - points[j][0])**2 + (points[i][1] - points[j][1])**2) # 两点距离
            if d < min_d:
                min_d = d                       # 修改最小距离
                min_ps = [points[i], points[j]] # 保存最近点对
    return min_ps
            


# 最接近点对（报错！）
def nearest_dot(seq):
    # 注意：seq事先已对x坐标排序
    n = len(seq)
    if n <= 2: return seq # 若问题规模等于 2，直接解决
    
    # 分解（子问题规模n/2）
    
    left, right = seq[0:n//2], seq[n//2:]
    
    mid_x = (left[-1][0] + right[0][0])/2.0
    # print(left, right,mid_x)

    # 递归，分治
    lmin = (left, nearest_dot(left))[len(left) > 2]    # 左侧最近点对
    rmin = (right, nearest_dot(right))[len(right) > 2] # 右侧最近点对
    # print (lmin,rmin,len(lmin))

    # 合并
    # dis_l = (float("inf"), get_distance(lmin))[len(lmin) > 1]
    if len(lmin)>1:
        dis_l = get_distance(lmin)
    else:
        dis_l = float("inf")
    # dis_r = (float("inf"), get_distance(rmin))[len(rmin) > 1]
    if len(rmin)>1:
        dis_r = get_distance(rmin)
    else:
        dis_r = float("inf")
    d = min(dis_l, dis_r)   # 最近点对距离

    # 处理中线附近的带状区域（近似蛮力）
    left = list(filter(lambda p:mid_x - p[0] <= d, left))   #中间线左侧的距离<=d的点
    right = list(filter(lambda p:p[0] - mid_x <= d, right)) #中间线右侧的距离<=d的点
    # print(left,right)
    mid_min = []
    for p in left:
        for q in right:
            if abs(p[0]-q[0])<=d and abs(p[1]-q[1]) <= d:     #如果右侧部分点在p点的(d,2d)之间
                td = get_distance((p,q))
                if td <= d: 
                    mid_min = [p,q]   # 记录p，q点对
                    d = td            # 修改最小距离
                    
    if mid_min:
        return mid_min
    elif dis_l>dis_r:
        return rmin
    else:
        return lmin


# 两点距离
def get_distance(min):
    # print (min)
    return sqrt((min[0][0]-min[1][0])**2 + (min[0][1]-min[1][1])**2)

def divide_conquer(seq):
    seq.sort(key=lambda x:x[0])
    res = nearest_dot(seq)
    return res
    
    
# 测试
seq=[(0,1),(3,2),(4,3),(5,1),(1,2),(2,1),(6,2),(7,2),(8,3),(4,5),(9,0),(6,4)]
# print(solve(seq)) # [(6, 2), (7, 2)]
print(divide_conquer(seq)) # [(6, 2), (7, 2)]