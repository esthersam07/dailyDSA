class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        d ={"2":"abc","3":"def","4":"ghi","5":"jkl","6":"mno","7":"pqrs","8":"tuv","9":"wxyz"}
        res = []
        
        def func(digits,d,i,cur):
            if len(cur)==len(digits):
                res.append(cur)
                return
            for c in d[digits[i]]:
                func(digits,d,i+1,cur+c)
        if digits:
            func(digits,d,0,"")
        return res
        