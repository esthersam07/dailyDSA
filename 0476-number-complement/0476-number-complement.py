class Solution:
    def findComplement(self, num: int) -> int:
        r = 0
        i = 0
        while num!=0:
            if num&1==0:
                r += 1<<i
            i+=1
            num>>=1
        return r
        