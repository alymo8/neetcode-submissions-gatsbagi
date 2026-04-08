class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        elif n == 2:
            return 2

        arr = [0] * (n +1)
        arr[n] = 1
        arr[n-1] = 1
        sum = 0

        for num in range(n-2, -1, -1):
            arr[num] = arr[num+1] + arr [num+2]
        return arr[0]
        