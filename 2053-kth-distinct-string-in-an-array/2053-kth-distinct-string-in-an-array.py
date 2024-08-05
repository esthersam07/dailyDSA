class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        d = {}
        res = []
        for s in arr:
            d[s] = 1+d.get(s,0)
        for s in d:
            if d[s]==1:
                res.append(s)
        if len(res)<k:
            return ""
        return res[k-1]