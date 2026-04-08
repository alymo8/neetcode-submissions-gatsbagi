class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        n = len(matrix)
        m = len(matrix[0])

        borderleft = 0
        borderup = 0
        borderdown = n - 1
        borderright = m -1

        result = []

        while borderleft <= borderright and borderup <= borderdown:
                # go right
                for j in range(borderleft, borderright + 1):
                    result.append(matrix[borderup][j])
                borderup += 1

                # go down
                for i in range(borderup, borderdown +1):
                    result.append(matrix[i][borderright])
                borderright -=1

                # go left
                if borderup <= borderdown:
                    for j in range(borderright, borderleft -1, -1):
                        result.append(matrix[borderdown][j])
                    borderdown -= 1

                # go up
                if borderleft <= borderright:
                    for i in range (borderdown, borderup -1, -1):
                        result.append(matrix[i][borderleft])
                    borderleft += 1
        return result