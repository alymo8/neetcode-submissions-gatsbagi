class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # iterate on borders
        # have a map with all what was visited, if we know it floods
        # dfs and see if from that border it goes to the other side or no, if yes
        # add all nodes in path to res.
       
        pacific = set()
        atlantic = set()
        rows = len(heights)
        cols = len(heights[0])

        def dfs(i, j, visited):
            if (i,j) in visited:
                return
            visited.add((i,j))
            neighbors = [(i-1, j), (i+1, j), (i,j-1), (i, j+1)]
            for ni,nj in neighbors:
                if 0 <= ni < rows and 0 <= nj < cols:
                    if heights[ni][nj] >= heights[i][j]:
                        dfs(ni,nj, visited)
        
        for i in range(rows):
            dfs(i, 0, pacific)
            dfs(i, cols-1, atlantic)
        for j in range(cols):
            dfs(0, j, pacific)
            dfs(rows-1, j, atlantic)
        return list(atlantic & pacific)

        