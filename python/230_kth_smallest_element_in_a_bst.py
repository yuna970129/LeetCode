# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        tree = []
        def convert_list(root):
            if not root:
                return
            convert_list(root.left)
            tree.append(root.val)
            if len(tree) == k:
                return
            convert_list(root.right)

        convert_list(root)
        return tree[k-1]
