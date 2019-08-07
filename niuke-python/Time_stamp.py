#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
    @File    :   Time_stamp.py
    @Time    :   2019/04/17 15:01:44
    @Author  :   R.
    @Version :   1.0
    @Contact :   827710637@qq.com
    @Desc    :   None
'''

'''
    根据Unix时间戳计算时间，不分大小月，每月30天，每年按360天计算。
    开始时间1970/01/01 00:00:00，输入秒数，显示时间
    例如，输入：
    2
    1
    12345678
    输出
    1970/01/01 00:00:01
    1970/05/23 21:21:18
'''

''' 
    time.localtime()能够实现真实时间的计算，不需要进行计算 
    time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    这个能够输出规格化的时间，但是时间是在1970-01-01 08:00:00开始的
'''

# here put the import lib
# import datetime

def Output_time(sec):

    Year_init = 1970
    Month_init = 1
    Day_init = 1
    Hour_init = 0
    Minute_init = 0

    while sec >= 60:
        sec -= 60
        Minute_init += 1
        if Minute_init == 60:
            Hour_init += 1
            Minute_init = 0
            if Hour_init == 24:
                Day_init += 1
                Hour_init = 0
                if Day_init == 31:
                    Month_init += 1
                    Day_init = 1
                    if Month_init == 13:
                        Year_init += 1
                        Month_init = 1
    #转为字符串
    year = str(Year_init)
    month = str(Month_init)
    day = str(Day_init)
    hour = str(Hour_init)
    minute = str(Minute_init)
    sec = str(sec)
    if len(month)==1:
        month = '0' + month
    if len(day)==1:
        day = '0' +day
    if len(hour) == 1:   #没有十位数，补0
        hour = '0' + hour
    if len(minute) == 1:
        minute = '0' + minute
    if len(sec) == 1:
        sec = '0' + sec
    time_str = year+'/'+month+'/'+day+' '+hour+':'+minute+':'+sec
    print (time_str)
    # print (Year_init,'/',Month_init,'/',Day_init,'  ',Hour_init,':',Minute_init,':',sec)
    # time_str = str(Year_init)+" "+str(Month_init)+" "+str(Day_init)+" "+str(Hour_init)+" "+str(Minute_init)+" "+str(sec)
    # print(datetime.datetime.strftime("%Y/%m/%d %H:%M:%S",time_str))

if __name__ == "__main__":

    seconds = int(input("Input seconds:"))

    if seconds < 0:
        print("Error.")
        import sys
        sys.exit()
    else:
        Output_time(seconds)
