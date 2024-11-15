class Solution:
    def findMin(self, nums: List[int]) -> int:
        arr = nums
        if len(arr)==1:
            return arr[0]
        l = 0
        r = len(arr)-1
        res = float('inf')
        while l<=r:
            m = (l+r)//2
            if r == l+1:
                return min(res,min(arr[l],arr[r]))
            elif arr[l]<arr[m]:
                res = min(res,arr[l])
                l = m+1
            else:
                res = min(res,arr[m])
                r = m-1
        return res
            
        