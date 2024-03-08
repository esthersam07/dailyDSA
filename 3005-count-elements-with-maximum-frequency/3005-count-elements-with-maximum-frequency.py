class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        d={}
        for i in nums:
            d[i]=1+d.get(i,0)
        res=0
        maxi={}
        m=0
        for j in d:
            if d[j]>m:
                maxi.clear()
                maxi[j]=d[j]
                m=d[j]
            elif d[j]==m:
                maxi[j]=d[j]
        for k in maxi:
            res+=maxi[k]
        return res
        
                
                
        