# -*- coding: utf-8 -*-

import os
import time

DATA_PATH = "D:\\myproject\\data\\account_book.txt"


def check():
    print 1

def charge_up():
    print 2

def account():
    print 3


def main():

    print '*' * 13, 'Account Book', '*' * 13
    account_book = open(DATA_PATH, "at+")
    # if account_book:
    #    print 'this is a account book'
    print '1.check ; 2.charge up ; 3.account ; 4.main ; 5.exit'
    while 1:
        chioce = eval(raw_input('Input your chioce :'))
        if chioce == 1:
            check()
        elif chioce == 2:
            charge_up()
        elif chioce == 3:
            account()
        elif chioce == 4:
            main()
        elif chioce == 5:
            exit()
    print '*' *10 ,'The Work is Down !','*' *10
    # print chioce
    account_book.close()


if __name__ == '__main__':
    main()
