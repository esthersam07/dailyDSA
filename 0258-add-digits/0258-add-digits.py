class Solution:
    def addDigits(self, num: int) -> int:
        while num>9:
            res = 0
            while num!=0:
                i = num%10
                res += i
                num = num//10
            num = res
        return num
        