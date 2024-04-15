class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        res=0
        c=start^goal
        while c>0:
            c=c&(c-1)
            res+=1
        return res
        