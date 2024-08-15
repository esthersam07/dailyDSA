class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        #5 - take 5
        #10 - take 10, return one 5 
        #20 - take 20, return(5,5,5) or (5,10)
        f = 0
        t = 0
        for b in bills:
            if b==5:
                f+=1
            elif b==10:
                if f>0:
                    f-=1
                    t+=1
                else:
                    return False
            else:
                if f>0 and t>0:
                    f-=1
                    t-=1
                elif f>=3:
                    f-=3
                else:
                    return False
        return True
        