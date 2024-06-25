class Solution:
    def trap(self, height: List[int]) -> int:
        #min(left(i),right(i))-a[i]
        l = 0
        r = len(height)-1
        maxL = 0
        maxR = 0
        res = 0
        while l<=r:
            if height[l]<=height[r]:
                if height[l]>=maxL:
                    maxL = height[l]
                else:
                    res += maxL-height[l]
                l+=1
            else:
                if height[r]>=maxR:
                    maxR = height[r]
                else:
                    res += maxR-height[r]
                r-=1
        return res