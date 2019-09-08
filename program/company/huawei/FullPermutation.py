#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
    @File    :   FullPermutation.py
    @Time    :   2019/09/08 21:52:52
    @Author  :   R.
    @Version :   1.0
    @Contact :   827710637@qq.com
    @Desc    :   None
'''

'''
    全排列
'''


# here put the import lib
def solution(nums):
    if not nums:
        return []
    
    res = []
    def backtrack(nums,tmp):
        if not nums:
            res.append(tmp)
            return 
        for i in range(len(nums)):
            backtrack(nums[:i] + nums[i+1:],tmp+[nums[i]])
    backtrack(nums,[])
    return res

def solution2(nums):
    # 去掉重复组合—nums中含有重复数字
    if not nums:
        return []
    nums.sort()
    n = len(nums)
    visited = [0] * n
    res = []
    def helper(tmp,length):
        if length == n:
            res.append(tmp)
        for i in range(n):
            if visited[i] or (i>0 and nums[i] == nums[i-1] and not visited[i-1]):
                continue
            visited[i] = 1
            helper(tmp+[nums[i]],length+1)
            visited[i] = 0
    helper([],0)
    return res

# print(solution([1,5,2,5,4]))
# print('-'*8)
# print(solution2([1,5,2,5,4]))
if len(solution([1,5,2,5,4])) == len(solution2([1,5,2,5,4])):
    print('-')
else:
    print('+')