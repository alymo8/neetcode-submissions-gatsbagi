class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1

        arr = [0] * (n +1)
        arr[n] = 1
        sum = 0

        for num in range(n-1, -1, -1):
            if num + 1 <= n:
                arr[num] += arr[num+1]
            if num + 2 <= n:
                arr[num] += arr [num+2]
        return arr[0]
        