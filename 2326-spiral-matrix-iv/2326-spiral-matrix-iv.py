# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        res = [[-1]*n for _ in range(m)]
        temp = head
        l = 0
        r = n
        t = 0
        b = m
        while(temp!=None):
            #move left to right
            for i in range(l,r):
                if temp!=None:
                    res[t][i] = temp.val
                    temp = temp.next
            t += 1
            #move top to bottom
            for i in range(t,b):
                if temp!=None:
                    res[i][r-1] = temp.val
                    temp = temp.next
            r -= 1
            
            # Traverse from right to left
            for i in range(r-1,l-1,-1):
                if temp!=None:
                    res[b-1][i] = temp.val
                    temp = temp.next
            b -= 1

            # Traverse from bottom to top
            for i in range(b-1,t-1,-1):
                if temp!=None:
                    res[i][l] = temp.val
                    temp = temp.next
            l += 1
            
        return res
        