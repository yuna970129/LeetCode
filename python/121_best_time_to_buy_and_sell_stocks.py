class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        b = prices[0]
        profit = 0

        for i in range(1, len(prices)):
            if b > prices[i]:
                b = prices[i]

            if prices[i] - b > profit:
                profit = prices[i] - b
        return profit