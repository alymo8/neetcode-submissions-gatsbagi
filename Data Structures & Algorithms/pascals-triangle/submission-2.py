class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = [[1]]
        # for i in range(2,numRows+1):
        #     res.append([0] * i)
        
        for i in range(1,numRows):
            res.append([0]*(i+1))
            for j in range(len(res[i])):
                if j-1 >= 0:
                    upleft = res[i-1][j-1]
                else:
                    upleft = 0
                if j < len(res[i-1]):
                    upright = res[i-1][j]
                else:
                    upright = 0
                
                res[i][j] = upleft + upright
            # res[i][-1] = 1

        return res






        