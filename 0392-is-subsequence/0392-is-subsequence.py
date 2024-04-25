class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s)==0:
            return True
        i=0
        j=0
        while i<len(s):
            if j>=len(t):
                return False
            if s[i]==t[j]:
                i+=1
                j+=1
            else:
                j+=1
        if i>=len(s):
            return True
        return False
                
        