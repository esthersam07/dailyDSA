class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        #sliding window
        res = 0
        l = 0
        r = 0
        z = 0
        while r<len(nums):
            if nums[r]==0:
                z +=1
            while z>k:
                if nums[l]==0:
                    z-=1
                l+=1
            temp = r-l+1
            res = max(res,temp)
            r+=1
        return res
        