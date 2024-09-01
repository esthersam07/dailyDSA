class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        res = []
        size = 0
        i = 0
        for r in range(m):
            temp = []
            for c in range(n):
                if i>=len(original):
                    return []
                temp.append(original[i])
                i+=1
                size += 1
            res.append(temp)
        if size!=m*n or i<len(original):
            return []
        return res
        