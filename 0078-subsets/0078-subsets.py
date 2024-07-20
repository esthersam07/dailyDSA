class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def func(arr,n,i,l,res):
            if i>=n:
                res.append(l[:])
                return 
            l.append(arr[i])
            func(arr,n,i+1,l,res)
            l.pop()
            func(arr,n,i+1,l,res)
        res=[]
        n = len(nums)
        func(nums,n,0,[],res)
        return res
        