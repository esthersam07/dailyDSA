class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        #finding non empty sub array sums       
        res = []
        for i in range(len(nums)):
            s = 0
            for j in range(i,len(nums)):
                s += nums[j]
                res.append(s)
        res.sort()
        
        sumi = 0
        if res[0]==0:
            res.pop(0)
        for i in range(left-1,right):
            sumi += res[i]
        return sumi%(10**9+7)
        