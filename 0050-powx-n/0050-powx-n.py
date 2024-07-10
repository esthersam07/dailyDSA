class Solution:
    def recurFunc(self,x,n,res):
        if n==0:
            return res
        if n%2==0:
            x = x*x
            n = n/2
        else:
            res = res*x
            n = n-1
        return self.recurFunc(x,n,res)
            
    def myPow(self, x: float, n: int) -> float:
        res = 1
        if n<0:
            n = abs(n)
            x = 1/x
        return self.recurFunc(x,n,res)