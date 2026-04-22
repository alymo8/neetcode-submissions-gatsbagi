class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profits = [0] * len(prices)

        
        for i in range(len(prices)-1, 0, -1):
            if prices[i] <= prices[i-1]:
                profits[i-1] = profits[i]
            else:
                profits[i-1] = profits[i] + prices[i] - prices[i-1]
        
        return profits[0]
                
        