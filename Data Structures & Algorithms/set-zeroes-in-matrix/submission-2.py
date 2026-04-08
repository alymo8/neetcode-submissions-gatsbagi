class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:

        n = len(matrix)
        m = len(matrix[0])

        is0row = set()
        is0col = set()
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 0:
                    is0row.add(i)
                    is0col.add(j)
        
        for row in is0row:
            for j in range(m):
                matrix[row][j] = 0
        for col in is0col:
            for i in range(n):
                matrix[i][col] = 0
       


        
        