# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    from collections import deque
    def isCompleteTree(self, root):
        if not root:
            return True

        queue = deque()
        queue.append(root)
        found_null = False

        while queue:
            node = queue.popleft()

            if node is None:
                found_null = True
            else:
                if found_null:
                    return False
                queue.append(node.left)
                queue.append(node.right)

        return True
            