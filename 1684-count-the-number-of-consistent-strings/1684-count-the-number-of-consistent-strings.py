class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        d = {}
        for c in allowed:
            d[c] = 1+d.get(c,0)
        l = d.keys()
        res = 0
        for  w in words:
            temp = {}
            for i in range(len(w)):
                if w[i] not in l:
                    break
                elif w[i] in l and i==len(w)-1:
                    res+=1
        return res