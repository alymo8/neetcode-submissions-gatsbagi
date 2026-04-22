class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        elif n == 2:
            return 2
        
        # total = 1
        total = 0
        left = 1
        right = 1
        
        for i in range(n-2, -1, -1):
            total = left + right
            right = left
            left = total
        return total