class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        temp = []
        for i in range(len(nums)):
            temp.append(nums[i])
        for i in range(len(temp)):
            c = (i+k)%len(temp)
            nums[c] = temp[i]
        return nums
        """
        Do not return anything, modify nums in-place instead.
        """
        