# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        if root==None:
            return 0
        q = deque()
        l = []
        q.append(root)
        while len(q)!=0:
            s = 0
            for _ in range(len(q)):
                if q[0].left!=None:
                    q.append(q[0].left)
                if q[0].right!=None:
                    q.append(q[0].right)
                s+=q[0].val
                q.popleft()
            l.append(s)
        if len(l)<k:
            return -1
        l.sort()
        return l[-k]
        
            
        