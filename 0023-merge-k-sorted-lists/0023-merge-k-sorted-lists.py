# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        tempList = []
        for l in lists:
            temp = l
            while temp!=None:
                tempList.append(temp.val)
                temp = temp.next
        tempList.sort()
        return self.listToLinkedList(tempList)
    def listToLinkedList(self,arr):
        d = ListNode()
        temp = d
        for i in arr:
            n = ListNode(i)
            temp.next = n
            temp = temp.next
        return d.next
        