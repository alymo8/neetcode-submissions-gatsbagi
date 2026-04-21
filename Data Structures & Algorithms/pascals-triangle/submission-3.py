class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = [[1]]
        
        for i in range(1,numRows):
            res.append([1]*(i+1))
            for j in range(1, i):
                # if j-1 >= 0:
                upleft = res[i-1][j-1]
            
                upright = res[i-1][j]

                
                res[i][j] = upleft + upright
            # res[i][-1] = 1

        return res






        