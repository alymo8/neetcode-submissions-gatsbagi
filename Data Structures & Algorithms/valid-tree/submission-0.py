class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
        adj_map = {i:[] for i in range(n)}
        for u,v in edges:
            adj_map.get(u,[]).append(v)
            adj_map.get(v,[]).append(u)
        visiting = set()
        seen = set()

        def traverse(node, prev):
            # if adj_map[node]== []:
            #     return True
            if node in visiting:
                return False
            visiting.add(node)
            for neighbor in adj_map[node]:
                if neighbor != prev and not traverse(neighbor, node):
                    return False
            seen.add(node)
            visiting.remove(node)
            return True

        if not traverse(0, None) or len(seen) != n:
            return False
        return True

        
        # for i in range(n):
        #     if not dfs(i):
        #         return False
