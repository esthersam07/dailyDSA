class Solution:
    def getLucky(self, s: str, k: int) -> int:
        temp = ""
        for c in s:
            temp += str(ord(c)-96)
        while k!=0:
            ss = 0
            for i in temp:
                ss += int(i)
            temp = str(ss)
            k -= 1
        return  int(temp)