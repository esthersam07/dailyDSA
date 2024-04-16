class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        #no. of subsets
        n = 1<<len(nums)
        res = []
        for x in range(0,n):
            l=[]
            for i in range(0,n):
                #check if ith bit is set in x
                if x&(1<<i):
                    l.append(nums[i])
            res.append(l)
        return res