class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        dp = [float('inf')] * (amount+1)
        dp[0] = 0

        for a in range(1,amount+1):
            for c in range(len(coins)):
                if coins[c] <= a:
                    dp[a] = min(dp[a], dp[a - coins[c]] + 1)
        return dp[amount] if dp[amount] != float('inf') else -1
