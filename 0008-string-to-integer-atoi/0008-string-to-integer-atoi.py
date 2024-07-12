class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.lstrip()
        
        if not s:
            return 0
        i =  0
        sign = 1
        if s[i]=="-":
            i += 1
            sign = -1
        elif s[i]=="+":
            i += 1
        res = 0
        while i<len(s):
            cur = s[i]
            if cur.isdigit():
                res = res*10+int(cur)
            else:
                break
            i+=1
        res *= sign
        
        if res>2**31-1:
            return 2**31-1
        elif res<=-2**31:
            return -2**31
        return res
        