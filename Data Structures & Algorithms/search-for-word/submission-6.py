class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if len(word) == 1:
            return any(word[0] in row for row in board)
        
        n = len(board)
        m = len(board[0])

        def check_next_char(i, j, k, visited):
            if k >= len(word):
                return False
            neighbors = [(i-1, j), (i+1, j), (i, j-1), (i,j+1)]
            for ni, nj in neighbors:
                if (0 <= ni < n and 0 <= nj < m) and (ni,nj) not in visited:
                    visited.add((ni,nj))
                    if board[ni][nj] == word[k]:
                        if k == len(word)-1:
                            return True
                        if check_next_char(ni,nj, k+1, visited):
                            return True
                    visited.remove((ni,nj))
            return False

        
        k = 0
        for i in range(n):
            for j in range(m):
                if board[i][j] == word[k]:
                    if check_next_char(i, j, k+1, {(i,j)}):
                        return True
        return False
       

        