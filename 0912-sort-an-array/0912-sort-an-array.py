class Solution:
    def merge(self,arr,l,m,r):
        left = arr[l:m+1]
        right = arr[m+1:r+1]
        i=j=0
        k = l
        while i<len(left) and j<len(right):
            if left[i]>=right[j]:
                arr[k] = right[j]
                j += 1
            else:
                arr[k] = left[i]
                i += 1
            k += 1
        while i<len(left):
            arr[k] = left[i]
            i += 1
            k += 1
        while j<len(right):
            arr[k] = right[j]
            j += 1
            k += 1
    def mergeSort(self,arr,l,r):
        if l==r:
            return arr
        m = (l+r)//2
        self.mergeSort(arr,l,m)
        self.mergeSort(arr,m+1,r)
        self.merge(arr,l,m,r)
        return arr
    def sortArray(self, nums: List[int]) -> List[int]:
        l = 0
        r = len(nums)-1
        return self.mergeSort(nums,l,r)