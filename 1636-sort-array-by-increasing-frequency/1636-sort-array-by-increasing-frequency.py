class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        count = Counter(nums)
        def func(n):
            return (count[n],-n)
        nums.sort(key=func)
        return nums
        