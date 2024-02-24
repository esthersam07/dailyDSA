class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        r=collections.defaultdict(list)
        c=collections.defaultdict(list)
        sq=collections.defaultdict(list)
        for i in range(9):
            for j in range(9):
                if board[i][j]==".":
                    continue
                if (board[i][j] in r[i]) or (board[i][j] in c[j]) or (board[i][j] in sq[(i//3,j//3)]):
                    return False
                r[i].append(board[i][j])
                c[j].append(board[i][j])
                sq[(i//3,j//3)].append(board[i][j])
        return True
        