class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        s = sum(chalk)
        r = k%s
        i = 0
        while r>=chalk[i]:
            r -= chalk[i]
            i += 1
            if i>=len(chalk):
                i = 0
        return i
        