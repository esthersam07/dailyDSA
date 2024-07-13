class Solution:
    mod = 10**9+7
    def power(self,x,y):
        if y==0:
            return 1
        ans = self.power(x,y//2)
        ans *= ans
        ans %= self.mod
        if y%2!=0:
            ans *= x
            ans %= self.mod
        return ans
    def countGoodNumbers(self, n: int) -> int:
        e = (n//2+n%2)
        o = n//2
        return (self.power(5,e)*self.power(4,o))%self.mod
        