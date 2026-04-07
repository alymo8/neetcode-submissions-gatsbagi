class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:

        is_0_row = set()
        is_0_col = set()
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    is_0_row.add(i)
                    is_0_col.add(j)
        
        for i in is_0_row:
            for k in range(len(matrix[0])):
                matrix[i][k] = 0
        for j in is_0_col:
            for k in range(len(matrix)):
                matrix[k][j] = 0
        