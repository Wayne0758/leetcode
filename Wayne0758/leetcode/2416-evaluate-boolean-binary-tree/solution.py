# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        if root == None:
            return None
        left = self.evaluateTree(root.left)
        right = self.evaluateTree(root.right)
        if root.val == 2:
            root.val = left or right
        if root.val == 3:
            root.val = left and right
        return root.val
