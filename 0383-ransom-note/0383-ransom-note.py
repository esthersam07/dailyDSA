class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        d1 = {}
        d2 = {}
        for c in ransomNote:
            d1[c] = 1+d1.get(c,0)
        for c in magazine:
            d2[c] = 1+d2.get(c,0)
        for x in d1:
            if x not in d2:
                return False
            if d1[x]>d2[x]:
                return False
        return True
        