# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    from collections import deque
    def zigzagLevelOrder(self, root):
        if root is None:
            return []
        res = []
        dq = deque([root])
        lefty = True

        while dq:
            level_size = len(dq)
            level_node = deque()
            for _ in range(level_size):
                node = dq.popleft()
                if lefty:
                    level_node.append(node.val)
                else:
                    level_node.appendleft(node.val)
                
                if node.left:
                    dq.append(node.left)
                if node.right:
                    dq.append(node.right)
            res.append(list(level_node))
            lefty = not lefty
        return res