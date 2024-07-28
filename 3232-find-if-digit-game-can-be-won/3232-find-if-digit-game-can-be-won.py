class Solution:
    def canAliceWin(self, nums: List[int]) -> bool:
        a_s = 0
        a_d = 0
        b = 0
        for i in nums:
            if 1<=i and i<=9:
                a_s+=i
            elif 10<=i and i<=99:
                a_d+=i
            else:
                b+=i
        if a_s>a_d+b:
            return True
        elif a_d>a_s+b:
            return True
        return False
        