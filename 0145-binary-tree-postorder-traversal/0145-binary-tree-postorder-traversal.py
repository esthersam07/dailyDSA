# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        '''1. Push root to first stack.
            2. Loop while first stack is not empty
                2.1 Pop a node from first stack and push it to second stack
                2.2 Push left and right children of the popped node to first stack
            3. Print contents of second stack
        '''
        if root is None:
            return []
        stack1 = []
        stack2 = []
        stack1.append(root)
        while(stack1):
            ele = stack1.pop()
            stack2.append(ele)
            if ele.left:
                stack1.append(ele.left)
            if ele.right:
                stack1.append(ele.right)
        result = []
        while stack2:
            node = stack2.pop()
            result.append(node.val)
    
        return result