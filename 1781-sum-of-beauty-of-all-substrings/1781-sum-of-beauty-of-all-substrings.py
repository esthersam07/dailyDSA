from collections import Counter
class Solution:
    def beautySum(self, s: str) -> int:
        res = 0
        for i in range(len(s)):
            multiSet = Counter()
            for j in range(i,len(s)):
                multiSet[s[j]] += 1
                maxi = max(multiSet.values())
                mini = min(multiSet.values())
                res += (maxi-mini)
        return res
        