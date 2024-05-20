# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def dfs(node, subNode):
            if node and subNode:
                if node.val == subNode.val:
                    return dfs(node.left, subNode.left) and dfs(node.right, subNode.right)
                else:
                    return False
            elif not node and not subNode:
                return True

        def search(node):
            if node:
                if node.val == subRoot.val and dfs(node, subRoot):
                    return True
                else:
                    if search(node.left):
                        return True
                    if search(node.right):
                        return True
            return False
        
        return search(root)
