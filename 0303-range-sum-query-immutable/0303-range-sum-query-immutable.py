class NumArray:
    arr = []
    def __init__(self, nums: List[int]):
        NumArray.arr = [0]
        for n in nums:
            NumArray.arr.append(n+NumArray.arr[-1])
        return
        

    def sumRange(self, left: int, right: int) -> int:
        return NumArray.arr[right+1]-NumArray.arr[left]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)