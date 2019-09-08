#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
    @File    :   test2.py
    @Time    :   2019/08/31 19:10:40
    @Author  :   R.
    @Version :   1.0
    @Contact :   827710637@qq.com
    @Desc    :   None
'''

'''
'''


# here put the import lib

if __name__ == "__main__":
    strlist = input()
    res = []
    stmp = ''
    if strlist:
        i = 0
        flag = False
        while i < len(strlist):
            c = strlist[i]
            if c == ',':
                if flag:
                    stmp += c
                else:
                    if len(stmp) == 0:
                        res.append('--')
                    else:
                        res.append(stmp)
                    stmp = ''
            elif c == '"':
                if i+1 < len(strlist) and strlist[i+1] == '"':
                    stmp += '"'
                    i += 1
                elif flag:
                    res.append(stmp)
                    stmp = ''
                    flag = False
                else:
                    flag = True
            else:
                stmp += c
            i += 1
        if len(stmp) != 0:
            res.append(stmp)
        if flag:
            print('ERROR')
        else:
            print(len(res))
            for i in res:
                print(i)
    else:
        print('1')
        print('--')
