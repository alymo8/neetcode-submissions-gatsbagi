class Solution:

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        n = len(board)
        m = len(board[0])
        rows = {}
        cols = {}
        squares = {}


        for i in range(n):
            if i not in rows:
                rows[i] = set()
            for j in range(m):
                if j not in cols:
                    cols[j] = set()
                if tuple([i,j]) not in squares:
                    squares[(i,j)] = set()
                cur = board[i][j]
                if cur != ".":
                    if cur in rows[i]:
                        return False
                    else:
                        rows[i].add(cur)
                    if cur in cols[j]:
                        return False
                    else:
                        cols[j].add(cur)
                    if cur in squares[(i//3,j//3)]:
                        return False
                    else:
                        squares[(i//3,j//3)].add(cur)
        return True
                    

        