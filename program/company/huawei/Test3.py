#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
    @File    :   Test3.py
    @Time    :   2019/09/07 20:22:34
    @Author  :   R.
    @Version :   1.0
    @Contact :   827710637@qq.com
    @Desc    :   None
'''

'''
    华为笔试第三题：
    题目描述：
    输入两个整数数组A和B，二者中元素都满足唯一且无序，同时A中的元素在B中都存在，B中元素在A中也存在，即A和B仅仅元素顺序可能不同，比如（1，3，5，2）和（3，2，1，5）。
    现在想通过分别删除A和B中的部分元素，使得A和B剩下的子序列完全相同，请输出数组A需要删除的最少元素数（注意数组B需要删除相同数量的元素）。
    输入描述：
    输入共三行，第一行为一个整数n（1<=n<=100000），表示A和B中元素的个数。第二行为数组A，共n个整数，第三行为数组B，共n个整数。
    输出描述：
    输出一行为数组A需要删除的元素数（包含换行）。
    输入：
    4
    1 3 5 2
    3 2 1 5
    输出：
    2
    说明：
    {1, 3, 5, 2}和{3, 2, 1, 5}的最长公共子序列有三个。分别为{1, 5}, {3, 5}, {3, 2}，所以至少需要删除2个元素。
    思路分析：
    首先用一个哈希表保存每个元素在A数组中的位置，接下来根据B的输入，利用A数组来保存对应元素的B中的位置。实质上对于A，B是需要查找二者相等元素的最长上升序列。
'''


# here put the import lib
def main_1():
    n = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    dp = [0] * (n+1)
    dp2 = [0] * (n+1)

    for i in range(n):
        for j in range(n):
            dp[j+1] = max(dp[j+1], dp2[j])
            if A[i] == B[j]:
                dp[j+1] = dp2[j] + 1
        dp2 = dp
    print(n-dp[n])


def lower_bound(arr, i, j, target):
    while i < j:
        mid = i + (j - i) // 2
        if target > arr[mid]:
            i = mid + 1
        else:
            j = mid
    return mid


def LIS(A, B):
    l = 1
    B[0] = A[0]
    for i in range(1, len(A)):
        if A[i] > B[l-1]:
            B[l] = A[i]
            l += 1
        else:
            p = lower_bound(B, 0, len(B), A[i])
            B[p] = A[i]
    return l


def main_2():
    n = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    M = dict()
    for i in range(n):
        M[A[i]] = i

    k = 0
    for i in range(n):
        A[M[B[i]]] = k
        k += 1
    # print(A, M)
    B = [0] * n
    ans = n - LIS(A, B)
    print(ans)


if __name__ == "__main__":
    main_2()
