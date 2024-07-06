class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        t = 0
        p = 1
        flag = True #true means have to move l to r
        while t!=time:
            if flag:
                if p==n:
                    flag = False
                else:
                    p+=1
                    t+=1
            elif flag==False:
                if p==1:
                    flag = True
                else:
                    p-=1
                    t+=1
        return p