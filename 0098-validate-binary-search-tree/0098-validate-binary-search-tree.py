# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def valid(node,lb,rb):
            if node==None:
                return True
            if not (node.val>lb and node.val<rb):
                return False
            return valid(node.left,lb,node.val) and valid(node.right,node.val,rb)
        
        return valid(root,float("-inf"),float("inf"))
        