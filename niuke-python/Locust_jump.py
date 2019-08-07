# -*- coding: utf-8 -*-


def Jump(x):

    step = 1
    location = 0
    count = 0
    if location == x:
        return count
    while location < x:
        if (location+step) >x:
            location -= step
            step += 1
            count += 1
        location += step
        step += 1
        count += 1

        if location == x:
            break 
    return count


if __name__ == "__main__":

    x = 10
    count = Jump(x)
    print count
