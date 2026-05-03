class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        n = len(board)
        m = len(board[0])

        def check_next_char(i, j, k):
            if k >= len(word):
                return True
            if i < 0 or i >= n or j < 0 or j >=m:
                return False
            if board[i][j] != word[k]:
                return False
            if board[i][j] == "#":
                return False
            temp = board[i][j]
            board[i][j] = "#"
            neighbors = [(i-1, j), (i+1, j), (i, j-1), (i,j+1)]
            found = False
            for ni, nj in neighbors:
                found = found or check_next_char(ni, nj, k+1)
            board[i][j] = temp
            return found

        for i in range(n):
            for j in range(m):
                if check_next_char(i, j, 0):
                    return True
        return False
       

        