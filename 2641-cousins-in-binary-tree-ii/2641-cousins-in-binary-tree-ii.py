# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def func(self,cur,l,lsum):
        if cur.left==None and cur.right==None:
            return
        if cur.left!=None and cur.right!=None:
            siblingSum = cur.left.val + cur.right.val
            cur.left.val = lsum[l] - siblingSum
            cur.right.val = lsum[l] - siblingSum
        elif cur.left==None:
            cur.right.val = lsum[l] - cur.right.val
        else:
            cur.left.val = lsum[l] - cur.left.val
        return 
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        #finding level sum of each level
        lsum = []
        ll = []
        q = deque()
        q.append(root)
        while len(q)!=0:
            size = len(q)
            s = 0
            subl = []
            for _ in range(size):
                if q[0].left!=None:
                    q.append(q[0].left)
                if q[0].right!=None:
                    q.append(q[0].right)
                subl.append(q[0])
                s+=q[0].val
                q.popleft()
            lsum.append(s)
            ll.append(subl)
        #curnode new value = level sum - curnode value -  siblings value
        root.val = 0
        l = 0
        for x in range(len(ll)):
            l = x+1
            for node in ll[x]:
                cur = node
                self.func(cur,l,lsum)
        return root