# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def kthSmallest(self, root, k):
        l = []
        def inorder(root):
            if root is None:
                return 
            inorder(root.left)
            l.append(root.val)
            inorder(root.right)
        inorder(root)
        
        for i in l:
            return l[k-1]