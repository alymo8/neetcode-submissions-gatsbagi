class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        INF = 2147483647
        n = len(grid)
        m = len(grid[0])

        q = deque([])
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 0:
                    q.append((i, j))
        
        val = 0
        while q:
            for _ in range(len(q)):
                i, j = q.popleft()
                neighbors = [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]
                for ni, nj in neighbors:
                    if 0 <= ni < n and 0 <= nj < m and grid[ni][nj] == INF:
                        grid[ni][nj] = val + 1
                        q.append((ni, nj))
            val += 1