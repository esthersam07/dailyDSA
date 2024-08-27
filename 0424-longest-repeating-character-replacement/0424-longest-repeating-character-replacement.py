class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        d = {}
        maxf = 0
        res = 0
        i = 0

        for j in range(len(s)):
            d[s[j]] = 1 + d.get(s[j], 0)
            maxf = max(maxf, d[s[j]])

            # If the current window size minus the max frequency character is greater than k, shrink the window
            while (j - i + 1) - maxf > k:
                d[s[i]] -= 1
                i += 1

            # Update the result with the size of the current valid window
            res = max(res, j - i + 1)

        return res
