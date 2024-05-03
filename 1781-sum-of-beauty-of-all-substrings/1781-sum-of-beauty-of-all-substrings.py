class Solution:
    def beautySum(self, s: str) -> int:
        res = 0
        for i in range(len(s)):
            d = {}
            for j in range(i,len(s)):
                d[s[j]] = 1+d.get(s[j],0)
                maxi = 0
                mini = 10**6
                for x in d:
                    maxi = max(maxi,d[x])
                    mini = min(mini,d[x])
                res += (maxi-mini)
        return res
        