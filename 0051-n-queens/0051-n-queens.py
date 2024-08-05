class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def isSafe(r,c,board,n):
            #check upper-left diagonal - both r,c dec
            tempr = r
            tempc = c
            while tempr>=0 and tempc>=0:
                if board[tempr][tempc]=='Q':
                    return False
                tempr -= 1
                tempc -= 1
            #check left column - r same, col dec
            tempc = c
            while tempc>=0:
                if board[r][tempc]=='Q':
                    return False
                tempc -= 1
            #check lower-left diagonal - r inc, c dec
            tempr = r
            tempc = c
            while tempr<n and tempc>=0:
                if board[tempr][tempc]=='Q':
                    return False
                tempr += 1
                tempc -= 1
            return True
        def func(c,board,ans,n):
            if c==n:
                ans.append([''.join(row) for row in board])
                return
            for r in range(n):
                if isSafe(r,c,board,n):
                    board[r][c] = 'Q'
                    func(c+1,board,ans,n)
                    board[r][c] = "."        # most imp-backtracking-removing q when moving back
        ans = []
        board = [["." for _ in range(n)] for _ in range(n)]
        func(0,board,ans,n)
        return ans