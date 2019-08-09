#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
    @File    :   494-TargetSum.py
    @Time    :   2019/08/09 16:37:14
    @Author  :   R.
    @Version :   1.0
    @Contact :   827710637@qq.com
    @Desc    :   DFS/01背包/动态
'''

'''
    给定一个非负整数数组，a1, a2, ..., an, 和一个目标数，S。
    现在你有两个符号 + 和 -。对于数组中的任意一个整数，你都
    可以从 + 或 -中选择一个符号添加在前面。
    返回可以使最终数组和为目标数 S 的所有添加符号的方法数。

'''


# here put the import lib

class Solution:
    def findTargetSumWays(self, nums, S):
        
        if not nums :
            return 0
        
        n = len(nums)
        # res = 0      
        # 超出时间限制
        # def dfs(index,tmp):
        #     nonlocal res
        #     if index == n :
        #         if  tmp  == S:
        #             res += 1
        #             return 
        #         else:
        #             return 
        #     dfs(index+1,tmp+nums[index])
        #     dfs(index+1,tmp-nums[index])
        # dfs(0,0)        
        # return res

        # 减少了部分计算，当i和i时的和在字典中时，不会计算。
        d = {}
        def dfs(index,tmp):
            if index < n and (index,tmp) not in d:
                d[(index,tmp)] = dfs(index+1,tmp+nums[index]) + dfs(index+1,tmp-nums[index])
            return d.get((index,tmp), int(tmp == S))
        
        return dfs(0,0)

    def findTargetSumWays2(self,nums,S):
        # 采用01背包，只有dfs的十分之一，动态的十分之一，核心思想还是动态
        if sum(nums) < S or (sum(nums) +S) %2 ==1:
            return 0
        # 逻辑：求nums最后等于S的组合，可推算为求一个子集的和为P，P=(sum(nums)+S)/2
        P = (sum(nums) + S)//2
        # dp:代表当和为dp[i]的时候，有几种组合，递推公式:dp[j] = dp[j-num] + dp[j]
        dp = [1] + [0 for _ in range(len(nums))]
        for num in nums:
            for j in range(P,num-1,-1):
                dp[j] += dp[j-num]
        return dp[P]

    def findTargetSumWays3(self,nums,S):
        length, dp = len(nums), {(0,0): 1}
        # 状态转移公式： dp[(i,j)] = dp.get((i - 1, j - nums[i]), 0) + dp.get((i - 1, j + nums[i]), 0)
        for i in range(1, length+1):
            for j in range(-sum(nums), sum(nums) + 1):
                dp[(i,j)] = dp.get((i - 1, j - nums[i-1]), 0) + dp.get((i - 1, j + nums[i-1]), 0)             
        return dp.get((length, S), 0)


so = Solution()
k = so.findTargetSumWays([1,1,1,1,1],3)
print(k)
