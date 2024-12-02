class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        lt = sentence.split(" ")
        l = len(searchWord)
        c = 1
        for w in lt:
            #print(w,w[:l])
            if w[:l]==searchWord:
                return c
            else:
                c+=1
        return -1
        