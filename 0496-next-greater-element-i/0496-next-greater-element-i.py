class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        d = {}
        for i,n in enumerate(nums1):
            for j in range(len(nums2)):
                if nums2[j]==n:
                    d[i] = j
            
        stack = []
        res = [-1]*len(nums2)
        
        for i in range(len(nums2)-1,-1,-1):
            while(stack and stack[-1]<=nums2[i]):
                stack.pop()
            if(stack):
                res[i] = stack[-1]
            stack.append(nums2[i])
        
        ans = []
        for k in d.values():
            ans.append(res[k])
        return ans
        