"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        
        if node == None:
            return None
        seen = {}

        def clone_node(node):
            if node.val in seen:
                return seen[node.val]
            copy_node = Node(node.val)
            seen[node.val] = copy_node
            for neighbor in node.neighbors:
                copy_node.neighbors.append(clone_node(neighbor))
            return copy_node
        return clone_node(node)

        