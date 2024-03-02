class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        l=0
        r=len(nums)-1
        temp=[]
        while l<=r:
            if (nums[l])**2>nums[r]**2:
                temp.append(nums[l]**2)
                l+=1
            else:
                temp.append(nums[r]**2)
                r-=1
        return temp[::-1]
                
        