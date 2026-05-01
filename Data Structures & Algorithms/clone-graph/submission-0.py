"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        seen = {}
        def copy_node(node):
            if node.val in seen:
                return seen[node.val]
            copy = Node(node.val)
            seen[copy.val] = copy
            for neighbor in node.neighbors:
                copy.neighbors.append(copy_node(neighbor))
            return copy
        if node == None:
            return None
        copy = copy_node(node)
        return copy
        