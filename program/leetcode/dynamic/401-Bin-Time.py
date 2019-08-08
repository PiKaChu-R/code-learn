#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
    @File    :   401-Bin-Time.py
    @Time    :   2019/08/08 17:37:33
    @Author  :   R.
    @Version :   1.0
    @Contact :   827710637@qq.com
    @Desc    :   None
'''

'''
二进制手表顶部有 4 个 LED 代表小时（0-11），底部的 6 个 LED 代表分钟（0-59）。
每个 LED 代表一个 0 或 1，最低位在右侧。
'''


# here put the import lib
class Solution:
    def readBinaryWatch(self, num):
        
        if num <0 or num > 8:
            return []
        
        if num == 0:
            return ['0:00']

        H_max = 3
        M_max = 5

        res = []

        def helper(h,m):
            if h < 0 or m < 0:
                return
            elif h >3:
                helper(h-1,m+1)
            else:
                tmp_h = []
                tmp_m = []
                for i in range(12):
                    if bin(i).count('1') == h:
                        tmp_h.append(str(i))
                for j in range(60):
                    # print(j,bin(j),bin(j).count('1'),m)
                    if (bin(j).count('1') == m):
                        if j<=9:
                            k = '0'+str(j)
                            print(k)
                            tmp_m.append(k)
                        else:
                            tmp_m.append(str(j))
                for i in tmp_h:
                    for j in tmp_m:
                        res.append(i+':'+j)
                
                helper(h-1,m+1)

        helper(num,0)
        
        return res
        


so = Solution()
k = so.readBinaryWatch(4)
print(k)



