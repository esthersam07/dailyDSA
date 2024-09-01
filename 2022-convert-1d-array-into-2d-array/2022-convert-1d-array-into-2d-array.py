class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        if m*n!=len(original):
            return []
        res = []
        for r in range(m):
            s = r*n
            e = s+n
            res.append(original[s:e])
        return res
        