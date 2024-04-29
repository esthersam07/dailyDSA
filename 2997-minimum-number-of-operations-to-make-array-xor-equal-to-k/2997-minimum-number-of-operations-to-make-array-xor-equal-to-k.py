class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        xor=0
        for i in nums:
            xor ^= i
        diff=0
        while xor!=0 or k!=0:
            if xor&1 != k&1:
                diff+=1
            xor>>=1
            k>>=1
        return diff