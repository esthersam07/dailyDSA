class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        res = 0
        for i in arr:
            if i%2!=0:
                res += 1
                if res==3:
                    return True
            else:
                res = 0
        return False
        