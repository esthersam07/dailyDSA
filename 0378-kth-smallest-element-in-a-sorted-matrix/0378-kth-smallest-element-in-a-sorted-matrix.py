class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        temp=[]
        m=len(matrix)
        n=len(matrix[0])
        for i in range(m):
            for j in range(n):
                temp.append(matrix[i][j])
        temp.sort()
        return temp[k-1]
        