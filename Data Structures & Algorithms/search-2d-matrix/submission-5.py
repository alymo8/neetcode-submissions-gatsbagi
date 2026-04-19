class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        up = 0
        down = len(matrix)-1
        row = -1
        while up <= down:
            mid = up + (down - up) // 2
            # if matrix[mid][0] <= target and mid+1 < len(matrix) and target < matrix[mid+1][0] or matrix[mid][0] <= target and mid+1 == len(matrix):
                
            if matrix[mid][0] <= target: # look down
                up = mid +1
                row = mid
            else: # matrix[mid][0] > target - look up 
                down = mid -1
        
        if row == -1:
            return False

        mid = row
        left = 0
        right = len(matrix[0]) -1
        while left <= right:
            midc = left + (right - left) // 2
            if matrix[mid][midc] == target:
                return True
            elif matrix[mid][midc] < target:
                left = midc+1
            elif matrix[mid][midc] > target:
                right = midc-1
        return False


