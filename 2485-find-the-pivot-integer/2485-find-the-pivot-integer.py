class Solution:
    def sumPrev(self,x:int):
            s=0
            for i in range(1,x+1):
                s+=i
            return s
    def aftPrev(self,x:int, n:int):
            s=0
            for i in range(x,n+1):
                s+=i
            return s
    def pivotInteger(self, n: int) -> int:
        l=1
        r=n
        
        while(l<=r):
            m=(l+r)//2
            if self.sumPrev(m)<self.aftPrev(m,n):
                l=m+1
            elif self.sumPrev(m)>self.aftPrev(m,n):
                r=m-1
            else:
                return m
        return -1