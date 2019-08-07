#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
    @File    :   Visit_museum.py
    @Time    :   2019/04/18 16:10:02
    @Author  :   R.
    @Version :   1.0
    @Contact :   827710637@qq.com
    @Desc    :   没看懂题意
'''

'''
    国家馆按顺序编号分别为0-9.
    如果玩的人太多，就把馆分成两批，分的方式是在相邻的某两个馆之间插一个牌子；
    任选其中一批先玩，另一批以后玩；
    如果一批馆还是玩不玩，则继续分为两批；
    一批中的馆全部玩完之后，才能玩下一个批馆；
    每批馆玩的时候，只能从这批当中编号最小的馆开始，按照相邻的编号逐个玩；
    一天至少可以玩一个馆。
    十个馆都玩完之后，小明拿出在十个馆盖章的册子，请你根据册子上盖章的顺序，判断小明是否遵守了自己的游玩方案。
    样例输入
    3287956401
    4130279856
    样例输出
    yes
    no
'''


# here put the import lib

def visit_museum(list_mus):


    for i in range(1,10):
        if (list_mus[i]-list_mus[i-1]) > 1:
            if i == 1 or list_mus[i-1] > list_mus[i-2]:
                j = 0
                flag = list_mus[i]-list_mus[i-1]-1
                count = 0
                while j < i-1:
                    if list_mus[j] < list_mus[i] and list_mus[j] > list_mus[i-1]:
                        count += 1
                    j += 1
                if count != flag:
                    return 0

    return 1


if __name__ == "__main__":

    k = input().strip().split()
    # print (k[0][0],type(k[0][0]))

    mus_list = []
    for i in range(len(k[0])):
        mus_list.append(int(k[0][i]))

    # print (mus_list)
    flag = visit_museum(mus_list)
    if flag == 0:
        print("No")
    else:
        print("Yes")