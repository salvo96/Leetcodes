class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 1:
            return 0

        left, right = 0, 1
        max_profit = 0

        while right < len(prices):
            if prices[left] > prices[right]:
                left = right
            else:
                profit = prices[right] - prices[left]
                max_profit = max(profit, max_profit)

            right += 1

        return max_profit
