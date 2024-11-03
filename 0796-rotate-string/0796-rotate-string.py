class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        l = list(s)
        temp = l
        g = list(goal)
        if l==g:
            return True
        for i in range(len(temp)):
            l.append(temp[i])
            l = l[1:]
            if l==g:
                return True
        return False