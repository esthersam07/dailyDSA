class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = 0
        ans = ""
        for i in range(len(s)):
            for j in range(i,len(s)):
                string = s[i:j+1]
                revString = string[::-1]
                if string == revString:
                    if res <= j-i+1:
                        res = j-i+1
                        ans = string
        return ans
        