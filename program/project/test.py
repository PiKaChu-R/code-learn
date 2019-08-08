# -*- coding: utf-8 -*-
def conversion_num(num, src, dest):
    rtn = ''
    # 1、校验源和目标是否相同
    if src == dest:
        rtn = num
    # 2、转成10进制#
    if src != 10:
        num_str = str(num)
        num_str = num_str[::-1]
        exe_num = 0
        dec_num = 0
        for num_char in num_str:
            # 十六进制处理
            if num_char == 'A':
                num_char = '10'
            elif num_char == 'B':
                num_char = '11'
            elif num_char == 'C':
                num_char = '12'
            elif num_char == 'D':
                num_char = '13'
            elif num_char == 'E':
                num_char = '14'
            elif num_char == 'F':
                num_char = '15'

            num_int = int(num_char)
            if exe_num == 0:
                dec_num += num_int
            else:
                dec_num += src ** exe_num * num_int
            exe_num += 1
        num = dec_num
    # 3、转成目标进制
    if dest == 10:
        rtn = num
    else:
        num = int(num)
        while True:
            divisor = num // dest
            remainder = num % dest
            # 十六进制处理
            if remainder == 10:
                remainder = 'A'
            elif remainder == 11:
                remainder = 'B'
            elif remainder == 12:
                remainder = 'C'
            elif remainder == 13:
                remainder = 'D'
            elif remainder == 14:
                remainder = 'E'
            elif remainder == 15:
                remainder = 'F'
            rtn = str(remainder) + rtn
            if divisor <= 0:
                break
            else:
                num = divisor
    # 4、处理空的字符串
    if rtn == '':
        rtn = '0'
    return rtn


new_num = conversion_num('111111', 2, 8)
print(new_num)