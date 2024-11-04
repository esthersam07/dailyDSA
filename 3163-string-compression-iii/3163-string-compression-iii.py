class Solution:
    def compressedString(self, word: str) -> str:
        res = ""
        i = 0
        while i<len(word):
            cur = word[i]
            c = 0
            while i<len(word) and c<9 and word[i]==cur:
                c+=1
                i+=1
            res+=str(c)
            res+=cur
        return res