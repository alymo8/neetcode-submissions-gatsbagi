class Solution:

    def validRow(self, cur, row, col, board, n, m):
        for j in range(m):
            if j != col and cur == board[row][j]:
                return False
        return True
    
    def validCol(self, cur, row, col, board, n, m):
        for i in range(n):
            if i != row and cur == board[i][col]:
                return False
        return True

    def validSquare(self, cur, row, col, board, n, m):

        #i = 2 -> 0,1,2
        #i = 5 -> 3,4,5

        # (i // 3) * 3
        # i 7 -> 2 * 3 = 6
        startRow = (row // 3) * 3
        startCol = (col // 3) * 3

        for i in range(startRow, startRow + 3):
            for j in range(startCol, startCol +3):
                if not (i == row and j == col) :
                    if cur == board[i][j]:
                        return False
        return True


    def isValidSudoku(self, board: List[List[str]]) -> bool:
        n = len(board)
        m = len(board[0])

        for i in range(n):
            for j in range(m):
                cur = board[i][j]
                if cur != ".":
                    if not self.validRow(cur, i, j, board, n, m):
                        return False
                    if not self.validCol(cur, i, j, board, n, m):
                        return False
                    if not self.validSquare(cur, i, j, board, n, m):
                        return False
        return True
                    

        