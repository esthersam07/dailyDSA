class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def backtrack(remaining, start, path, results):
            if remaining == 0:
                results.append(list(path))
                return
            if remaining < 0:
                return
            
            for i in range(start, len(candidates)):
                path.append(candidates[i])
                backtrack(remaining - candidates[i], i, path, results)
                path.pop()
        
        results = []
        backtrack(target, 0, [], results)
        return results
        