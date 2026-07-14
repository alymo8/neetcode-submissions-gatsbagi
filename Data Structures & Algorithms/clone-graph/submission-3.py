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

        def cloneNode(node):
            if node in seen:
                return seen[node]
            copy_node = Node(node.val)
            seen[node] = copy_node
            for neighbor in node.neighbors:
                copy_neighbor = cloneNode(neighbor)
                copy_node.neighbors.append(copy_neighbor)
            
            return copy_node
        return cloneNode(node)
            