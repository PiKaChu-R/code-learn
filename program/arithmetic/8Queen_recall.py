#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
    @File    :   8Queen_recall.py
    @Time    :   2019/06/21 10:39:34
    @Author  :   R.
    @Version :   1.0
    @Contact :   827710637@qq.com
    @Desc    :   回溯法解决8皇后问题
'''

'''
思路：一行一行的放置皇后，判断皇后的位置是否符合条件，当放置到最后一行时，则所有皇后
    的位置放置完毕，保存棋盘活棋盘数加一。
'''


# here put the import lib

max_coordinate = 8
queen_list = [None]*8


def check(column):
    column_2 = 0
    while column_2 < column:
        if (queen_list[column_2] == queen_list[column]) or \
                (abs(queen_list[column_2]-queen_list[column]) == (column-column_2)):
            return False
        column_2 += 1
    return True


def show():
    column = 0
    while column < max_coordinate:
        print('(%d %d)'% (queen_list[column],column),end=" ")
        column+=1
    print ("")


def put_queen(column):
    # 采用回溯算法
    row = 0  # 表示行号

    while row < max_coordinate:
        # 对行进行遍历
        queen_list[column] = row

        if check(column):
            # 对列进行检查
            if column == max_coordinate-1:
                show()
            else:
                put_queen(column+1)

        row += 1

def queen(queen_list,current_column =0):
    
    for row in range(len(queen_list)):
        if current_column == len(queen_list):
            for i in range(len(queen_list)):
                print("(%d %d)"%(queen_list[i],i),end=" ")
            print("")
            return 
        queen_list[current_column],flag = row,True
        for column in range(current_column):
            if (queen_list[column]==row) or\
                (abs(row - queen_list[column]) == current_column - column):
                flag = False
                break
        
        if flag:
            queen(queen_list,current_column+1)

if __name__ == "__main__":
    # put_queen(4)
    queen(queen_list)