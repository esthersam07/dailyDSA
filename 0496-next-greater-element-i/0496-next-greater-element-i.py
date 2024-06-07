class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        d = {}
        for i in nums1:
            for ind in range(len(nums2)):
                if nums2[ind]==i:
                    d[i] = [ind,-1]
        res = []
        for i in d:
            ans = d[i][0]
            while ans<len(nums2):
                if nums2[ans]>i:
                    d[i][1] = nums2[ans]
                    break
                ans += 1
            res.append(d[i][1])
        return res
        