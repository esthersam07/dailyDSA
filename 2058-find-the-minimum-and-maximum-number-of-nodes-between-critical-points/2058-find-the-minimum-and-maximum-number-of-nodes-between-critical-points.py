# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        res = []
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
            #local minima
            elif l.val>temp.val and temp.val<r.val:
                res.append(c)
            c+=1
            l = temp
            temp = temp.next
            
        if len(res)<2:
            return [-1,-1]
        
        mini = 10**9
        maxi = res[-1] - res[0]
        for i in range(1,len(res)):
            mini = min(mini,res[i]-res[i-1])
    
        return [mini, maxi]
        