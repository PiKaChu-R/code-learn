class Solution:
    def canPartition(self, nums):
        # 动态规划 - 01背包
        size = len(nums)
        s = sum(nums)
        if s & 1 ==1:
            return False

        target = s//2
        dp = [False for _ in range(target+1)]

        # 状态转移方程 ：dp[i-1][j] = dp[i-1][j] or dp[i-1][j-nums[i]]
        # 单独1个数可以构成子集，根据状态转移方程，当 j == nums[i] 的时候成立，会来看dp[i-1][0]的值
        # 因此根据语义，dp[0]应该设置为True
        dp[0] = True

        for j in range(target+1):
            if nums[0] == j:
                dp[j] = True
                break
        
        for i in range(1,size):
            dp[-1] = dp[-1] or dp[target-nums[i]]
            if dp[-1]:
                return True

            for j in range(target-1,-1,-1):
                if j >= nums[i]:
                    dp[j] = dp[j] or dp[j-nums[i]]
                else:
                    break
        return dp[-1]

            

so = Solution()
k = so.canPartition([1,2,3,4,5,6,7])
print(k)



