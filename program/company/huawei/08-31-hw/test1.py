
if __name__ == "__main__":
    n = int(input())
    n_b = bin(n)[2:]
    print(n_b)
    count = 0
    index = -1

    for i in range(len(n_b),2,-1):
        if n_b[i-3:i] == '101':
            count += 1
            index = i-3
    
    print(count,index)