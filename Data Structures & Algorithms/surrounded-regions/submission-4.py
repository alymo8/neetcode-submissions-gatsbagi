class Solution:

    def update_group(self, i, j, rows, cols, board, border_connected):
        if i - 1 >= 0 and board[i-1][j] == 'O' and border_connected[i-1][j] == 0:
            border_connected[i-1][j] = 1
            self.update_group(i-1, j, rows, cols, board, border_connected)
        if i + 1 < rows and board[i+1][j] == 'O' and border_connected[i+1][j] == 0:
            border_connected[i+1][j] = 1
            self.update_group(i+1, j, rows, cols, board, border_connected)
        if j - 1 >= 0 and board[i][j-1] == 'O' and border_connected[i][j-1] == 0:
            border_connected[i][j-1] = 1
            self.update_group(i, j-1, rows, cols, board, border_connected)
        if j + 1 < cols and board[i][j+1] == 'O' and border_connected[i][j+1] == 0:
            border_connected[i][j+1] = 1
            self.update_group(i, j+1, rows, cols, board, border_connected)
        return border_connected
    def solve(self, board: List[List[str]]) -> None:
        rows = len(board)
        cols = len(board[0])
        if rows < 2 or cols < 2:
            return

        border_connected = [[0 for _ in range(cols)] for _ in range(rows)]

        for i in [0, rows-1]:
            for j in range(0, cols):
                if board[i][j] == "O":
                    border_connected[i][j] = 1
                    border_connected = self.update_group(i, j, rows, cols, board, border_connected)
        for j in [0, cols-1]:
            for i in range(0, rows):
                if board[i][j] == "O":
                    border_connected[i][j] = 1
                    border_connected = self.update_group(i, j, rows, cols, board, border_connected)


        for i in range(1, rows - 1):
            for j in range(1, cols - 1):
                if board[i][j] == "O" and border_connected[i][j] == 0:
                    board[i][j] = "X"