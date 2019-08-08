#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
    @File    :   test_py2.py
    @Time    :   2019/08/08 16:53:56
    @Author  :   R.
    @Version :   1.0
    @Contact :   827710637@qq.com
    @Desc    :   动态规划
'''

'''
    1105.填充书架：
    你把要摆放的书 books 都整理好，叠成一摞：从上往下，第 i 本书的厚度为 
    books[i][0]，高度为 books[i][1]。
    按顺序 将这些书摆放到总宽度为 shelf_width 的书架上。    
    先选几本书放在书架上（它们的厚度之和小于等于书架的宽度 shelf_width），
    然后再建一层书架。重复这个过程，直到把所有的书都放在书架上。
    需要注意的是，在上述过程的每个步骤中，摆放书的顺序与你整理好的顺序相同。 
    例如，如果这里有 5 本书，那么可能的一种摆放情况是：第一和第二本书放在
    第一层书架上，第三本书放在第二层书架上，第四和第五本书放在最后一层书架上。
    每一层所摆放的书的最大高度就是这一层书架的层高，书架整体的高度为各层高之和。
    以这种方式布置书架，返回书架整体可能的最小高度。
'''


# here put the import lib

class Solution:
    def minHeightShelves(self, books, shelf_width):
        # 动态规划。
        n = len(books)
        # 放置第i本书的最大高度，dp[0]为未放置书籍的高度，为0.
        dp = [float('inf')] * (n+1)
        dp[0] = 0

        for i in range(1,n+1):
            tmp_width,j,h = 0,i,0
            while j > 0:
                # 从第i-1本（多取了个0，因此减1）往前加，当宽度不超过规定宽度时，判断最小高度。
                tmp_width += books[j-1][0]
                if tmp_width > shelf_width:
                    break
                h = max(h,books[j-1][1])
                # 递推公式，dp[i] = min(dp[i],dp[j-1]+h)
                dp[i] = min(dp[i],dp[j-1]+h)
                j -= 1
        return dp[-1]
        


so = Solution()
k = so.minHeightShelves([[1,1],[2,3],[2,3],[1,1],[1,1],[1,1],[1,2]],4)
print(k)



