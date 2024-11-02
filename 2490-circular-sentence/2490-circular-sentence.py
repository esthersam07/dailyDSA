class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        l = list(map(str,sentence.split()))
        n = len(l)
        if l[0][0] != l[n-1][-1]:
            return False
        
        i = 0
        j = 1
        while j<n:
            if l[i][-1]!=l[j][0]:
                return False
            i+=1
            j+=1
        return True