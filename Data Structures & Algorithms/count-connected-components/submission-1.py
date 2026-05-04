class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        res = 0

        adj_list = {}

        for u, v in edges:
            adj_list.setdefault(u, []).append(v)
            adj_list.setdefault(v, []).append(u)
        
        def dfs(node):
            if node in adj_list:
                if adj_list[node] ==  [-1]:
                    return
                neighbors = adj_list[node]
                adj_list[node] = [-1]
                for neighbor in neighbors:
                    dfs(neighbor)
            return
        
        for i in range(n):
            if i in adj_list and adj_list[i] !=  [-1]:
                res += 1
                dfs(i)
            elif i not in adj_list:
                res += 1
        return res
            
                