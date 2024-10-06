# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q = deque()
        ll = []
        if(root==None):
            return ll
        q.append(root)
        while(len(q)!=0):
            size = len(q)
            subl = []
            for _ in range(size):
                if(q[0].left!=None):
                    q.append(q[0].left)
                if(q[0].right!=None):
                    q.append(q[0].right)
                subl.append(q[0].val)
                q.popleft()
            ll.append(subl)
        return ll
            
        