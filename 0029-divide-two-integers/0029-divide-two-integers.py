class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        sign = True
        n = dividend
        d = divisor
        if d==1:
            return n
        if (d>0 and n<0) or (d<0 and n>0):
            sign = False
            
        n = abs(dividend)
        d = abs(divisor)
        
        ans=0
        while(n>=d):
            c=0
            while(d*(2**(c+1)))<=n:
                c+=1
            ans+=(2**c)
            n-=d*(2**c)
        if ans>(2**31)-1:
            return (2**31) -1
        elif ans<(-2**31):
            return -2**31
                        
        if sign:
            return ans
        else:
            return -ans
        