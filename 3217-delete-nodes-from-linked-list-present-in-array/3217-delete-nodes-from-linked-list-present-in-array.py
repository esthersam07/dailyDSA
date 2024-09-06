# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        s = set(nums) # for O(1) lookup
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        cur = head
        
        while cur!=None:
            if cur.val in s:
                n = cur.next
                prev.next = n
                cur.next = None
                cur = n
            else:
                prev = cur
                cur = cur.next
        return dummy.next
                
        