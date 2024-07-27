class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        def func(arr,i,l,res):
            res.append(list(l))
            for x in range(i,len(arr)):
                if x!=i and arr[x]==arr[x-1]:
                    continue
                l.append(arr[x])
                func(arr,x+1,l,res)
                l.pop()
        nums.sort()
        res = []
        func(nums,0,[],res)
        return res
        