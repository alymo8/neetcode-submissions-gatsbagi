class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        adj_list = {}

        for u, v in edges:
            adj_list.setdefault(u, []).append(v)
            adj_list.setdefault(v, []).append(u)
        
        def dfs(node):
            if node in adj_list:
                if adj_list[node] == [-1]:
                    return
                neighbors = adj_list[node]
                adj_list[node] = [-1]
                for neighbor in neighbors:
                    dfs(neighbor)

            return
        
        result = 0
        for node in range(n):
            if node not in adj_list:
                result += 1
            elif node in adj_list and adj_list[node] != [-1]:
                result += 1
                dfs(node)
        return result
        
                