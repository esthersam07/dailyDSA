class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        def func(l,r,temp,i,nums):
            while l<=r:
                m = (l+r)//2
                if temp[m]==nums[i]:
                    break
                elif temp[m-1]<nums[i] and nums[i]<temp[m]:
                    temp[m]=nums[i]
                    break
                elif nums[i]<temp[m]:
                    r=m-1
                elif nums[i]>temp[m]:
                    l=m+1
            return temp
        #using binary search
        temp =[]
        for i in range(len(nums)):
            if len(temp)==0:
                temp.append(nums[i])
            elif nums[i]>temp[-1]:
                temp.append(nums[i])
            elif nums[i]<temp[0]:
                temp[0] = nums[i]
            else:
                temp = func(0,len(temp)-1,temp,i,nums)
        return len(temp)