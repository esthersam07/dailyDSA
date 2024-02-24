class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        r={0:[],1:[],2:[],3:[],4:[],5:[],6:[],7:[],8:[]}
        c={0:[],1:[],2:[],3:[],4:[],5:[],6:[],7:[],8:[]}
        sq={(0,0):[],(0,1):[],(0,2):[],(1,0):[],(1,1):[],(1,2):[],(2,0):[],(2,1):[],(2,2):[]}
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
        