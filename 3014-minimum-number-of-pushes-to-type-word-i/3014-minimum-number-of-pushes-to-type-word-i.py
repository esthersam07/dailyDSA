class Solution:
    def minimumPushes(self, word: str) -> int:
        res = 0
        c = 0
        for x in word:
            if c<8:
                res += 1
                c+=1
            elif c>=8 and c<16:
                res += 2
                c+=1
            elif c>=16 and c<24:
                res += 3
                c+=1
            else:
                res += 4
                c+=1
        return res
        