class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n<=0:
            return False
        inv = n-1
        if n&inv==0:
            return True
        return False
        