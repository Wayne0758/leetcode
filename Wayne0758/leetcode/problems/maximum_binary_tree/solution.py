# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if len(nums)==0:
            return None
        mx=-float('inf')
        mx_idx=0
        for i in range(len(nums)):
            if nums[i]>mx:
                mx=nums[i]
                mx_idx=i
        root=TreeNode(mx)
        leftarr=nums[:mx_idx]
        rightarr=nums[mx_idx+1:]
        root.left=self.constructMaximumBinaryTree(leftarr)
        root.right=self.constructMaximumBinaryTree(rightarr)
        return root