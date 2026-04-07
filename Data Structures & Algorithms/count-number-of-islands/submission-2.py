class Solution:

    def fill_all_island(self, i, j, rows, cols, grid):
        grid[i][j] = '2'
        if i - 1 >= 0 and grid[i-1][j] == '1':
            self.fill_all_island(i-1, j, rows, cols, grid)
        if i + 1 < rows and grid[i+1][j] == '1':
            self.fill_all_island(i+1, j, rows, cols, grid)
        if j - 1 >= 0 and grid[i][j-1] == '1':
            self.fill_all_island(i, j-1, rows, cols, grid)
        if j + 1 < cols and grid[i][j+1] == '1':
            self.fill_all_island(i, j + 1, rows, cols, grid)


    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0
        rows = len(grid)
        columns = len(grid[0])

        for i in range(rows):
            for j in range(columns):
                if grid[i][j] == '1':
                    self.fill_all_island(i, j, rows, columns, grid)
                    islands +=1 
        return islands

        