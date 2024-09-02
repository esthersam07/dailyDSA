class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        s = sum(chalk)
        r = k%s
        i = 0
        while r>=chalk[i]:
            r -= chalk[i]
            i += 1
            #full rounds of the array got removed by k%s. So we won't need complete a round and cpome back again in the front
            if i>=len(chalk):
                i = 0
        return i
        