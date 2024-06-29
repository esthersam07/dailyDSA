# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        q = deque()
        res = []
        if root == None:
            return res
        flag = 0 #0 - L to R
        q.append(root)
        
        while(len(q)!=0):
            sub = []
            for i in range(len(q)):
                node = q.popleft()
                if(node.left!=None):
                    q.append(node.left)
                if(node.right!=None):
                    q.append(node.right)
                sub.append(node.val)
            if flag == 0:
                res.append(sub)
                flag = 1
            else:
                res.append(sub[::-1])
                flag = 0
        return res
        