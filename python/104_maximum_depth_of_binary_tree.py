# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def depth(root, d):
            if root is None:
                return d
            left_d = depth(root.left, d + 1)
            right_d = depth(root.right, d + 1)
            return max(left_d, right_d)

        return depth(root, 0)
