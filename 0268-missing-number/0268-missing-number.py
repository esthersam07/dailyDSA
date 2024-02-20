class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        xor1=0
        xor2=0
        for i in range(1,len(nums)+1):
            xor1=xor1^i
            xor2=xor2^nums[i-1]
        return xor2^xor1