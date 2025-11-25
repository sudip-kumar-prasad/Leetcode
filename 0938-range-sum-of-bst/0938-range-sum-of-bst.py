# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rangeSumBST(self, root, low, high):
        l = []
        def inorder(root):
            if root is None:
                return 
            inorder(root.left)
            l.append(root.val)
            inorder(root.right)
        inorder(root)
        c = 0
        for i in l:
            if low <= i <= high:
                c += i
        return c