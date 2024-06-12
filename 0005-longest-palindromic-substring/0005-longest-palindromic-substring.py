class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        length = 0
        for i in range(len(s)):
            #odd lengths
            l = i
            r = i
            while l>=0 and r<len(s) and s[l]==s[r]:
                if r-l+1>length:
                    res = s[l:r+1]
                    length = r-l+1
                l-=1
                r+=1
                
            #even lengths
            l = i
            r = i+1
            while l>=0 and r<len(s) and s[l]==s[r]:
                if r-l+1>length:
                    res = s[l:r+1]
                    length = r-l+1
                l-=1
                r+=1
        return res
        