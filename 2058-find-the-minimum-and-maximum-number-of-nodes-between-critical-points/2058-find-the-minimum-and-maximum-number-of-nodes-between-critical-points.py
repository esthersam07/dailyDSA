# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        res = []
        mini = 10**9
        maxi = 0
        l = head
        c = 1
        temp = head.next
        if l.next==None or temp.next == None:
            return [-1,-1]
        while temp.next!=None:
            r = temp.next
            #local maxima
            if l.val<temp.val and temp.val>r.val:
                res.append(c)
                mini = min(mini,c)
                maxi = max(maxi,c)
            elif l.val>temp.val and temp.val<r.val:
                res.append(c)
                mini = min(mini,c)
                maxi = max(maxi,c)
            c+=1
            l = temp
            temp = temp.next
        if len(res)<2:
            return [-1,-1]
        min_distance = float('inf')
        max_distance = res[-1] - res[0]
    
        for i in range(1, len(res)):
            min_distance = min(min_distance, res[i] - res[i - 1])
    
        return [min_distance, max_distance]
        