class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        def func(arr,k,n,i,l,res):
            if len(l)==k and n==0:
                res.append(list(l))
                return
            if i>=len(arr) or len(l)>k:
                return
            l.append(arr[i])
            func(arr,k,n-arr[i],i+1,l,res)
            l.pop()
            func(arr,k,n,i+1,l,res)
        arr = [1,2,3,4,5,6,7,8,9]
        res = []
        func(arr,k,n,0,[],res)
        return res
        