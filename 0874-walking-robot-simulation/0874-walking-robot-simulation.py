class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        x,y = 0,0
        d = [[0,1],[1,0],[0,-1],[-1,0]]
        res = 0
        direct = 0
        obstacles = {tuple(o) for o in obstacles}
        for c in commands:
            if c==-1:
                direct = (direct+1)%4 #we do mod length of the d array for the cases when d goes out of bounds
            elif c==-2:
                direct = (direct-1)%4
            else:
                for _ in range(c):
                    dx,dy = d[direct]
                    if (x+dx,y+dy) in obstacles:
                        break
                    x,y = x+dx,y+dy
            res = max(res,x**2+y**2)
        return res
        
        
        
        