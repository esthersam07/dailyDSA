# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        '''if head.next==None and n==1:
            return None'''
        l = 0
        cur = head
        while cur!=None:
            l+=1
            cur = cur.next
        if l==n:
            return head.next
        p = 0
        prev = ListNode(0)
        prev.next = head
        cur = head
        while p<(l-n):
            p+=1
            prev = cur
            cur = cur.next
        prev.next = cur.next
        cur.next = None
        return head
        
        