class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        ind = 0
        for i in range(len(word)):
            if word[i]==ch:
                ind = i
                break
            elif i==len(word)-1:
                return word
        f = word[:i+1]
        f = f[::-1]
        l = word[i+1:]
        return f+l