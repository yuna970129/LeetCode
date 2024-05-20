# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        depth = defaultdict(list)
        def dfs(r, cnt):
            if not r:
                return
            depth[cnt].append(r.val)
            dfs(r.left, cnt+1)
            dfs(r.right, cnt+1)
        
        dfs(root, 0)

        return depth.values()
