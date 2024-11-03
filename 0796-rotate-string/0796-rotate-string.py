class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(s)!=len(goal):
            return False
        s = s+s
        i = 0
        j = len(goal)
        while j<len(s):
            if s[i:j]==goal:
                return True
            i+=1
            j+=1
        return False