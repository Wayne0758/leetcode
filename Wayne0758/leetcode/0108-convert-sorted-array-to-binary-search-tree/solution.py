# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if len(nums)==0:
            return None
        elif len(nums)==1:
            return TreeNode(nums[0])
        mid = int(len(nums)/2)
        root=TreeNode(nums[mid])
        root.right=self.sortedArrayToBST(nums[mid+1:len(nums)])
        root.left=self.sortedArrayToBST(nums[0:mid])
        return root
