# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        p1 = collections.deque([p])
        q1 = collections.deque([q])
        if not p and not q:
            return True
        if not p or not q:
            return False
        while p1 and q1:
            nodep = p1.popleft()
            nodeq = q1.popleft()
            leftsame=False
            rightsame=False
            if not nodep.left or not nodeq.left:
                if nodep.left == nodeq.left:
                    leftsame=True
            else:
                if nodep.left.val == nodeq.left.val:
                    leftsame=True
            if not nodep.right or not nodeq.right:
                if nodep.right == nodeq.right:
                    rightsame=True
            else:
                if nodep.right.val == nodeq.right.val:
                    rightsame=True
            if nodep.val != nodeq.val or not leftsame or not rightsame:
                return False
            if nodep.left:
                p1.append(nodep.left)
            if nodep.right:
                p1.append(nodep.right)
            if nodeq.left:
                q1.append(nodeq.left)
            if nodeq.right:
                q1.append(nodeq.right)
        return True
