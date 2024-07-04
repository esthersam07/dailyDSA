# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        newHead = ListNode(-1)
        temp = newHead
        l = head
        r = head.next
        while r!=None:
            res = 0
            while r.val!=0:
                res += r.val
                r = r.next
            l = r
            r = l.next
            node = ListNode(res)
            temp.next = node
            temp = node
        return newHead.next