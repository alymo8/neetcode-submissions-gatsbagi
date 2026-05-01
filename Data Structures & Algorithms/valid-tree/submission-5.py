class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
        adj_map = {i:[] for i in range(n)}
        for u,v in edges:
            adj_map.get(u,[]).append(v)
            adj_map.get(v,[]).append(u)
        seen = set()

        def traverse(node, parent):
            if node in seen:
                return False
            seen.add(node)
            for neighbor in adj_map[node]:
                if neighbor == parent:
                    continue
                if not traverse(neighbor, node):
                    return False
            
            return True

        return traverse(0, None) and len(seen) == n