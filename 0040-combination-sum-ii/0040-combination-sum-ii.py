class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        def func(arr,target,pos,l,res):
            if target==0:
                res.append(l.copy())
                return
            if target<=0:
                return
            prev = -1
            for i in range(pos,len(arr)):
                if prev==arr[i]:
                    continue
                l.append(arr[i])
                func(arr,target-arr[i],i+1,l,res)
                l.pop()
                prev = arr[i]
            
        candidates.sort()
        res = []
        func(candidates,target,0,[],res)
        return res
        