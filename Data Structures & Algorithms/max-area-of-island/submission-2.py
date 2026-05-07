class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def dfs(i, j):
            if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] != 1:
                return 0
            grid[i][j] = -1

            neighbors = [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]
            res = 1
            for ni, nj in neighbors:
                res += dfs(ni, nj)
            return res
        res = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    res = max(res, dfs(i, j))
        return res