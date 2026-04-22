class Solution:
    def tribonacci(self, n: int) -> int:
        prev = 0
        t0, t1, t2 = 0, 1, 1
        if n == 0:
            return t0
        elif n == 1 or n == 2:
            return t1

        cur = 0
        for i in range(3,n+1):
            
            cur = t0 + t1 + t2
            t0 = t1
            t1 = t2
            t2 = cur
        return cur


