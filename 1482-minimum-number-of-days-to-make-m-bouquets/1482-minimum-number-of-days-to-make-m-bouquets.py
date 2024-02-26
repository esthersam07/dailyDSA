class Solution:
    def possible(self, arr: List[int],day: int, m: int, k: int) -> bool:
        n = len(arr)  # size of the array
        cnt = 0
        noOfB = 0
        # count the number of bouquets
        for i in range(n):
            if arr[i] <= day:
                cnt += 1
            else:
                noOfB += cnt // k
                cnt = 0
        noOfB += cnt // k
        return noOfB >= m
    
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if m*k>len(bloomDay):
            return -1
        l=min(bloomDay)
        r=max(bloomDay)
        while l<=r:
            day=(l+r)//2
            if self.possible(bloomDay,day,m,k):
                r=day-1
            else:
                l=day+1
        
        return l
        