class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        d={}
        for i in nums:
            d[i] = 1+d.get(i,0)
        res=[]
        for x in d:
            if d[x]==1:
                res.append(x)
        return res