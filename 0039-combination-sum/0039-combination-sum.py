class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def func(arr, k, i,s, l, res):
            if s == k:
                res.append(l.copy())
                return
            if i >= len(arr) or s>k:
                return
            l.append(arr[i])
            func(arr, k,i, s+arr[i], l, res)
            l.pop()
            func(arr, k, i + 1,s, l, res)
        
        res = []
        func(candidates, target, 0,0, [], res)
        return res
        