# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        res = []
        for r in range(m):
            row = []
            for c in range(n):
                row.append(-1)
            res.append(row)
        temp = head
        l = 0
        r = n
        t = 0
        b = m
        while(l<r and t<b):
            #move left to right
            for i in range(l,r):
                if temp==None:
                    break
                res[t][i] = temp.val
                temp = temp.next
            t += 1
            #move top to bottom
            for i in range(t,b):
                if temp==None:
                    break
                res[i][r-1] = temp.val
                temp = temp.next
            r -= 1
            
            if (t < b) :
                # Traverse from right to left
                for i in range(r-1,l-1,-1):
                    if temp==None:
                        break
                    res[b-1][i] = temp.val
                    temp = temp.next
                b -= 1

            if (l < r) :
                # Traverse from bottom to top
                for i in range(b-1,t-1,-1):
                    if temp==None:
                        break
                    res[i][l] = temp.val
                    temp = temp.next
                l += 1

            
        return res
        