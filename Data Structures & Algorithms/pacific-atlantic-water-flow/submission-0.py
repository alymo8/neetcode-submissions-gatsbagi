class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # iterate on borders
        # have a map with all what was visited, if we know it floods
        # dfs and see if from that border it goes to the other side or no, if yes
        # add all nodes in path to res.
        pacific = set()
        atlantic = set()
        res= []

        def dfs(i, j, visited, is_pacific):
            if tuple([i,j]) in visited:
                return
            visited.add((i,j))
            neighbors = [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]
            for k, l in neighbors:
                if 0 <= k < len(heights) and 0 <= l < len(heights[0]):
                    if heights[k][l] >= heights[i][j]:
                        resp = dfs(k, l, visited, is_pacific)
                        if resp and [k,l] not in res:
                            res.append([k,l])
                        

        
        rows = len(heights)
        cols = len(heights[0])

        for i in range(rows):
            dfs(i, 0, pacific, True)
            dfs(i, cols-1, atlantic, False)
        
        for j in range(cols):
            dfs(0, j, pacific, True)
            dfs(rows-1, j, atlantic, False)
            
        return list(pacific & atlantic)
        