class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        d1 = {}
        d2 = {}
        for i in nums1:
            d1[i] = 1+d1.get(i,0)
        for j in nums2:
            d2[j] = 1+d2.get(j,0)
        res = []
        for x in d1:
            if x in d2:
                if d1[x]==d2[x]:
                    for y in range(d1[x]):
                        res.append(x) 
                elif d1[x]<d2[x]:
                    for y in range(d1[x]):
                        res.append(x)
                else:
                    for y in range(d2[x]):
                        res.append(x)
        return res
                    
        