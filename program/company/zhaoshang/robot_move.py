if __name__ == "__main__":
    s = input()
    n = len(s)
    nums = [0] * len(s)

    for i in range(len(s)):
        if s[i] == 'R':
            j = i+1
            count = 1
            while j < n and s[j] != 'L':
                j += 1
                count += 1
            if (10*100 - count)%2 == 0:
                nums[j] += 1
            else:
                nums[j-1] += 1
        elif s[i] == 'L':
            j = i-1
            count = 1
            while j >=0 and s[j] != 'R':
                j -= 1
                count += 1
            if (10**100 - count ) % 2 == 0:
                nums[j] += 1
            else:
                nums[j+1] += 1
    ans = ' '.join(str(i) for i in nums)
    print(ans)