class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        d = {}
        for i,n in enumerate(nums1):
            d[n] = i
            
        stack = []
        res = [-1]*len(nums1)
        
        for i in range(len(nums2)):
            cur = nums2[i]
            while(stack and stack[-1]<cur):
                val = stack.pop()
                res[d[val]] = cur
            if cur in d:
                stack.append(cur)
        
        return res
        