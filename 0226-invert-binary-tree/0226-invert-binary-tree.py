# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def invertTree(self, root):
        if root is None:
            return None
        right_in = self.invertTree(root.right)
        left_in = self.invertTree(root.left)
        root.left = right_in
        root.right = left_in
        
        return root

        