"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        
        queue = deque([node]) # 1
        clones = {node.val: Node(node.val, [])} # clones.items() = [1]

        while queue:
            clone = queue.popleft() # clone.val = 1
            print(clone.val)

            for n in clone.neighbors: # 2,4
                if n.val not in clones:
                    queue.append(n) # 2
                    clones[n.val] = Node(n.val, [])
                clones[n.val].neighbors.append(clones[clone.val])
        return clones[node.val]
