class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l=0
        r=0
        s=0
        minl=10**9
        while r<len(nums):
            s+=nums[r]
            while s>=target:
                minl=min(minl,r-l+1)
                s-=nums[l]
                l+=1
            r+=1
        if minl==10**9:
            return 0
        else:
            return minl
        