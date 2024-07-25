class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def func(arr, k, i, l, res):
            if k == 0:
                res.append(list(l))
                return
            if i == len(arr):
                return
            if arr[i] <= k:
                l.append(arr[i])
                func(arr, k - arr[i], i, l, res)
                l.pop()
            func(arr, k, i + 1, l, res)
        
        res = []
        func(candidates, target, 0, [], res)
        return res
        