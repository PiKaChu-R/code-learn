class Solution:
    def findMaxForm(self, strs, m, n):
               
        # if not strs :
        #     return 0
        
        count_num = []
        for s in strs:
            s0 = s.count('0')
            s1 = len(s)-s0
            count_num.append((s0,s1))

        # 动态规划超时 
        # 状态转移方程 dp[i][j] = max(dp[i][j],dp[i-c_0][j-c_1]+1)
        # dp = [[0]*(n+1) for _ in range(m+1)]

        # for ind in range(len(strs)):
        #     c_0 = count_num[ind][0]
        #     c_1 = count_num[ind][1]
        #     for i in range(m,c_0-1,-1):
        #         for j in range(n,c_1-1,-1):
        #             dp[i][j] = max(dp[i-c_0][j-c_1]+1,dp[i][j])
        # return dp[m][n]

        # 贪心算法
        def _findMaxFrom(s,m,n):
            count = 0
            for k in s:
                if m >=k[0] and n>=k[1]:
                    count += 1
                    m -= k[0]
                    n -= k[1]
            return count
        
        # 按0或1计数里面较小者从小到大排序  
        s1 = sorted(count_num,key = lambda i:min(i[0],i[1]))
        # 取该字符后剩余0或者1计数里较小者从大到小排序
        s2 = sorted(count_num, key = lambda i:min(m-i[0],n-i[1]), reverse = True)
        return max(_findMaxFrom(s1,m,n),_findMaxFrom(s2,m,n))


so = Solution()
k = so.findMaxForm(["10","0001","111001","1","0"],5,3)
print(k)



