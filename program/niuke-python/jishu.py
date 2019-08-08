import os
import sys
if __name__ == "__main__":

    # k = os.path.realpath(__file__)
    k = sys.path[0]
    paths = os.walk(k)
    count = -1
    for _, _, name in paths:
        for i in name:
            file = os.path.splitext(i)
            filename, type_1 = file
            if type_1 == '.py':
                count += 1

    # count = count - 1
    print(count)
