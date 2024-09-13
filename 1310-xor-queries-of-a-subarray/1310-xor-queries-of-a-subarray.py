class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        ps = [0] #prefixsum array
        for i in arr:
            ps.append(i^ps[-1])
        res = []
        for q in queries:
            s = q[0] #staring index
            e = q[1] #ending index
            res.append(ps[e+1]^ps[s])
        return res
        