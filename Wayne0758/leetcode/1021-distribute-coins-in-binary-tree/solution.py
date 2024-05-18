# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self, res=0):
        self.res = res
    def helper(self, node: Optional[TreeNode]) -> int:
        if node == None:
            return 0
        left = self.helper(node.left)
        right = self.helper(node.right)
        self.res += abs(left) + abs(right)
        return node.val + left + right - 1
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        self.res = 0
        self.helper(root)
        return self.res
