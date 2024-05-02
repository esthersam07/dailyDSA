class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        res = -1
        for i in nums:
            if -i in nums and i>res:
                res = i
        return res