# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flipEquiv(self, r1: Optional[TreeNode], r2: Optional[TreeNode]) -> bool:
        #base case
        if r1==None or r2==None:
            if r1==None and r2==None:
                return True
            else:
                return False
        if r1.val != r2.val:
            return False
        
        a = self.flipEquiv(r1.left,r2.left) and self.flipEquiv(r1.right,r2.right)
        return a or self.flipEquiv(r1.left,r2.right) and self.flipEquiv(r1.right,r2.left)