class Solution:
    def myAtoi(self, str: str) -> int:
        
        new_str = str.strip()
        if len(new_str)<=0:
            return 0
        if len(new_str) == 1 and (new_str[0] =='-' or new_str[0] =='+'):
            return 0

        str = ''
        if new_str[0] =='-' or new_str[0] =='+' or '0'<=new_str[0]<='9':
            str = new_str[0] + str
        else:
            return 0
        for i in range(1,len(new_str)):
            if '0'<=new_str[i]<='9':
                str+=new_str[i]
            else:
                break
        
        if len(str) >=1 and (str[0] !='-' or str[0] !='+'):
            num = int(str)
            if -2**31<num<2**31-1:
                return num
            if num<0:
                return -2147483648
            else:
                return 2147483647
        return 0

if __name__ == "__main__":
    s = "+-2"
    m = Solution()
    k = m.myAtoi(s)
    print(k)