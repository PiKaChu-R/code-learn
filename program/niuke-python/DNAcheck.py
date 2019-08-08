import sys

def longest_str(word,DNA):
    
    n = len(word)
    count = [0]*n
    # print (count)
    if word[0] in DNA:
        count[0] = 1
    for i in range(1,n):
        if word[i] in DNA:
            count[i] = count[i-1]+1
            
    return max(count)
if __name__=="__main__":
    word_key = input('Input the str:')
    key_DNA = ['A','T','C','G']
    num = longest_str(word_key,key_DNA)
    print(num)