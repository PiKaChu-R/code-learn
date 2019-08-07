import sys


def repeat(list_word):

    count = 0
    set_word = set(list_word)
    if len(set_word) == len(list_word):
        return len(list_word)
    dict_word = {}
    for i in set_word:
        dict_word[i] = list_word.count(i)
    # print(dict_word)
    for key in dict_word.keys():
        count += dict_word[key]%2
        # 两个偶数处理有问题
    return count


if __name__ == "__main__":

    list_word = list(input())
    num = repeat(list_word)
    print(num)
