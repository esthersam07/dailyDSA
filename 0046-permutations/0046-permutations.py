class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def func(arr,l,freq,res):
            if len(l)==len(arr):
                res.append(list(l))
                return
            for i in range(len(arr)):
                if freq[i]==0:
                    l.append(arr[i])
                    freq[i] = 1
                    func(arr,l,freq,res)
                    l.pop()
                    freq[i] = 0
            
        res = []
        freq = [0]*len(nums)
        func(nums,[],freq,res)
        return res
        