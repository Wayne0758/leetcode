# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.hashmap = dict()
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        self.hashmap = collections.defaultdict(int)
        for i in range(len(postorder)):
            self.hashmap[postorder[i]] = i
        return self.helper(preorder, postorder, 0, len(preorder)-1, 0, len(postorder)-1)
    def helper(self, preorder: List[int], postorder: List[int], prestart: int, preend: int, poststart: int, postend: int) -> Optional[TreeNode]:
        if prestart > preend or poststart > postend:
            return None
        root = TreeNode(preorder[prestart])
        if (prestart+1) <= preend:
            pivot = self.hashmap[preorder[prestart+1]]-poststart
            root.left = self.helper(preorder, postorder, prestart+1, prestart+1+pivot, poststart, poststart+pivot)
            root.right = self.helper(preorder, postorder, prestart+1+pivot+1, preend, poststart+pivot+1, postend-1)
        return root
