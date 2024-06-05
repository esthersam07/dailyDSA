class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        d = {}
        for i,n in enumerate(nums1):
            d[n] = i
        res = [-1]*len(nums1)
        for i in range(len(nums2)):
            if nums2[i] not in nums1:
                continue
            for j in range(i+1, len(nums2)):
                if nums2[j]>nums2[i]:
                    idx = d[nums2[i]]
                    res[idx] = nums2[j]
                    break
        return res