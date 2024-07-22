class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        d={}
        for i in range(len(names)):
            d[heights[i]]=names[i]
        new = dict(sorted(d.items()))
        res = []
        for x in new:
            res.append(new[x])
        return res[::-1]
        