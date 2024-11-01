class Solution:
    def makeFancyString(self, s: str) -> str:
        res = ""
        freq = 0
        for c in s:
            if len(res)==0:
                res += c
                freq = 1
            elif c==res[-1]:
                res += c
                freq += 1
                if freq==3:
                    res = res[:-1]
                    freq -= 1
            else:
                res+=c
                freq = 1
        return res