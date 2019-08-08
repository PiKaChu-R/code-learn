#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
    @File    :   Boss_intelligence.py
    @Time    :   2019/04/19 14:54:33
    @Author  :   R.
    @Version :   1.0
    @Contact :   827710637@qq.com
    @Desc    :   None
'''

'''
    BOSS会列出一正整数的序列，由小萌先开始，然后两个人轮流从序列的任意一端取数，
    取得的数累加到积分里，当所有数都取完，游戏结束。
    假设小萌和BOSS都很聪明，两个人取数的方法都是最优策略，问最后两人得分各是多少。
    输入
    第一行：一个正整数N（2 ≤ N ≤ 100），表示序列中正整数的个数。
    第二行至末尾：用空格隔开的N个正整数（1 ≤ a[i] ≤ 200）
    输出
    只有一行，用空格隔开的两个数，小萌的得分和BOSS的得分。
    样例输入
    6
    4 7 2 9 5 2
    样例输出
    18 11
'''


# here put the import lib

def Calcul_goal(num):

    M_list = []
    B_list = []
    print(num,len(num))
    for i in range(len(num)):
        if len(num)-1 > 2:
            # a_1, a_2, b_1, b_2 = 0
            a_1 = num[1]
            a_2 = num[-1]
            b_1 = num[0]
            b_2 = num[-2]
            # print(a_1, a_2, b_1, b_2)
            if a_1 > b_1 or a_1 > b_2 or a_2 > b_1 or a_2 > b_2:
                M_list.append(num[0])
                num = num[1:]
                if num[0] > num[-1]:
                    B_list.append(num[0])
                    num = num[1:]
                else:
                    B_list.append(num[-1])
                    num = num[:-1]
            else:
                M_list.append(num[-1])
                num = num[:-1]
                if num[0] > num[-1]:
                    B_list.append(num[0])
                    num = num[1:]
                else:
                    B_list.append(num[-1])
                    num = num[:-1]
        elif len(num) == 2:
            if num[0] > num[1]:
                M_list.append(num[0])
                num = num[1:]
                B_list.append(num[0])
            else:
                M_list.append(num[-1])
                num = num[:-1]
                B_list.append(num[0])
        elif len(num) == 1:
            break
    # print (M_list,B_list)
    count = 0
    for i in range(len(M_list)):
        count += M_list[i]
    return count


if __name__ == "__main__":
    k = int(input("The len of num:"))
    num_1 = input("Num:").strip().split()
    if len(num_1) != k:
        import sys
        print('Error.')
        sys.exit()
    list_num = []
    sum_list = 0
    for i in range(k):
        list_num.append(int(num_1[i]))
        sum_list += int(num_1[i])
    print (list_num)
    result = Calcul_goal(list_num)

    print("小萌：",sum_list-result,"Boss:",result)
