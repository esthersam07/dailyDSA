class Solution:
    def minimumPushes(self, word: str) -> int:
        '''  9 - 16  = 2
            17 - 24 = 3
            25 - 26 = 4'''
        d = {}
        for c in word:
            d[c] = 1+d.get(c,0)
        l = []
        for x in d:
            l.append(d[x])
        l.sort()
        lt=l[::-1]
        print(lt)
        res = 0
        c = 0
        for x in lt:
            if c<8:
                res += x
                c+=1
            elif c>=8 and c<16:
                res += (x*2)
                c+=1
            elif c>=16 and c<24:
                res += (x*3)
                c+=1
            else:
                res += (x*4)
                c+=1
        return res
        