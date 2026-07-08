class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        n = len(grid)
        m = len(grid[0])

        def fill_out_island(i, j):
            if grid[i][j] != '1':
                return

            grid[i][j] = '-1'
            neighbors = [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]
            for ni, nj in neighbors:
                if ni >= 0 and ni < n and nj >= 0 and nj < m:
                    fill_out_island(ni, nj)

        num_islands = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == '1':
                    fill_out_island(i, j)
                    num_islands += 1
        return num_islands