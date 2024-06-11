# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        n = mountain_arr.length()

        # Helper function to find the peak element index
        def findPeak():
            l, r = 0, n - 1
            while l < r:
                m = (l + r) // 2
                if mountain_arr.get(m) < mountain_arr.get(m + 1):
                    l = m + 1
                else:
                    r = m
            return l
        
        # Helper function for binary search
        def binarySearch(l, r, target, isAsc):
            while l <= r:
                m = (l + r) // 2
                curr = mountain_arr.get(m)
                if curr == target:
                    return m
                if isAsc:
                    if curr < target:
                        l = m + 1
                    else:
                        r = m - 1
                else:
                    if curr < target:
                        r = m - 1
                    else:
                        l = m + 1
            return -1
        
        peak = findPeak()
        
        # Try to find target in the ascending part
        index = binarySearch(0, peak, target, True)
        if index != -1:
            return index
        
        # Try to find target in the descending part
        return binarySearch(peak + 1, n - 1, target, False)

# Example of how you might use the class:
# solution = Solution()
# result = solution.findInMountainArray(target, mountain_arr_instance)
