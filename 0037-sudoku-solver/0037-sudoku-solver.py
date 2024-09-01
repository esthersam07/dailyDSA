class Solution:
    def isValid(self,b,r,c,x):
        for i in range(9):
            if b[r][i]==str(x):
                return False
            if b[i][c]==str(x):
                return False
            if b[3*(r//3)+i//3][3*(c//3)+i%3]==str(x):
                return False
        return True
    def solve(self,b):
        for i in range(9):
            for j in range(9):
                if b[i][j]==".":
                    for c in range(1,10):
                        if self.isValid(b,i,j,c):
                            b[i][j]=str(c)
                            if self.solve(b):
                                return True
                            else:
                                b[i][j] = "."
                    return False
        return True
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        return self.solve(board)
        