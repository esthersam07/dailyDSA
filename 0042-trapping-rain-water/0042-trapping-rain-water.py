class Solution:
    def trap(self, height: List[int]) -> int:
        prefixMaxHt = [0]*len(height)
        pmht = 0
        for i in range(len(height)):
            pmht = max(pmht,height[i])
            prefixMaxHt[i] = pmht
        suffixMaxHt = [0]*len(height)
        smht = 0
        for i in range(len(height)-1,-1,-1):
            smht = max(smht,height[i])
            suffixMaxHt[i] = smht
        res = 0
        for i in range(len(height)):
            res += min(prefixMaxHt[i],suffixMaxHt[i])-height[i]
        return res
        