class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        count=0
        l=len(nums)
        nums.sort()
        for a in range(l-1,1,-1):
            b=0
            c=a-1
            while b<c:
                if nums[b]+nums[c]>nums[a]:
                    count+=c-b
                    c-=1
                else:
                    b+=1
        return count
        