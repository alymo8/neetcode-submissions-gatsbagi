class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        n = len(grid)
        m = len(grid[0])
        res = 0

        def fill_island(i, j):
            if i < 0 or i >= n or j < 0 or j >= m:
                return
            if grid[i][j] != "1":
                return
            grid[i][j] = -1
            neighbors = [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]
            for ni, nj in neighbors:
                fill_island(ni, nj)
            

        for i in range(n):
            for j in range(m):
                if grid[i][j] == "1":
                    fill_island(i, j)
                    res+=1
        return res