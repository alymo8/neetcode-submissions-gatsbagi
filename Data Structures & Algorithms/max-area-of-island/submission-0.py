class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        val = 0
        def dfs(i, j):
            nonlocal val

            if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] != 1:
                return 0
            val += 1
            grid[i][j] = -1

            neighbors = [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]
            for ni, nj in neighbors:
                dfs(ni, nj)
        
        res = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    dfs(i, j)
                    res = max(res, val)
                    val = 0
        return res