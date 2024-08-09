class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        def func(i,j,r,c,grid):
            d = {1:1,2:1,3:1,4:1,5:1,6:1,7:1,8:1,9:1}
            dd = {1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0}
            #check sum of rows
            rsum = 0
            for y in range(j,j+2+1):
                rsum += grid[i][y]
                if 1<=grid[i][y] and grid[i][y]<=9 and dd[grid[i][y]]==0:
                    dd[grid[i][y]] = 1
            for x in range(i+1,i+2+1):
                temp = 0
                for y in range(j,j+2+1):
                    temp += grid[x][y]
                    if 1<=grid[x][y] and grid[x][y]<=9 and dd[grid[x][y]]==0:
                        dd[grid[x][y]] = 1
                if temp!=rsum:
                    return False
                
            #check sum of columns
            csum = 0
            for x in range(i,i+2+1):
                csum += grid[x][j]
                if 1<=grid[x][j] and grid[x][j]<=9 and dd[grid[x][j]]==0:
                    dd[grid[x][j]] = 1
            if csum != rsum:
                return False
            for y in range(j+1,j+2+1):
                temp = 0
                for x in range(i,i+2+1):
                    temp += grid[x][y]
                    if 1<=grid[x][y] and grid[x][y]<=9 and dd[grid[x][y]]==0:
                        dd[grid[x][y]] = 1
                if temp != csum:
                    return False
                
            #check sum of diagonals
            dsum = 0
            x = i
            y = j
            while x<i+3 and y<j+3:
                dsum += grid[x][y]
                if 1<=grid[x][y] and grid[x][y]<=9 and dd[grid[x][y]]==0:
                    dd[grid[x][y]] = 1
                x += 1
                y += 1
            if dsum != csum :
                return False
            dsum2 = 0
            x = i+2
            y = j
            while x>=i and y<j+3:
                dsum2 += grid[x][y]
                if 1<=grid[x][y] and grid[x][y]<=9 and dd[grid[x][y]]==0:
                    dd[grid[x][y]] = 1
                x -= 1
                y += 1
            if dsum2 != dsum:
                return False
            if dd!=d:
                return False
            return True
        res = 0
        r = len(grid)
        c = len(grid[0])
        for i in range(r-2):
            for j in range(c-2):
                if func(i,j,r,c,grid):
                        res+=1
        return res
        