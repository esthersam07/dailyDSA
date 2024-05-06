# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp = head
        stack = []
        while temp:
            while len(stack)!=0 and temp.val>stack[-1]:
                stack.pop()
            stack.append(temp.val)
            temp = temp.next
        dumm = ListNode()
        temp = dumm
        for i in stack:
            temp.next = ListNode(i)
            temp = temp.next
        return dumm.next;
        