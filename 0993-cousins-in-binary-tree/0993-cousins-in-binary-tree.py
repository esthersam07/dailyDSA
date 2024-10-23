# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findLevelnP(self,root,x):
        q = deque()
        q.append([root,None])
        l = 0
        while len(q)!=0:
            size = len(q)
            for _ in range(size):
                cur, parent = q.popleft()
                if cur.val==x:
                    return (l,parent)
                if cur.left!=None:
                    q.append([cur.left,cur])
                if cur.right!=None:
                    q.append([cur.right,cur])
            l+=1
        return (-1,None)
        
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        xl,xp = self.findLevelnP(root,x)
        yl,yp = self.findLevelnP(root,y)
        if xl==yl and xp!=yp:
            return True
        return False
        