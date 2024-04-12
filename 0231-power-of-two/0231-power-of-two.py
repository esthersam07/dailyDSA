class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n<=0:
            return False
        c=0
        n=bin(n).lstrip('0b')
        for i in n:
            if i=='1' and c>0:
                return False
            elif i=='1':
                c+=1
        return True
        