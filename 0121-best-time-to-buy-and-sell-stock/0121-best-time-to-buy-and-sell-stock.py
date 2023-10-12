class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        dp = [0 for i in range(len(prices))]

        max_value = 0
        best_value = 0

        for i in range(len(prices) - 1, -1, -1):
            if i == len(prices) - 1:
                max_value = prices[i]
                continue
            if prices[i] >= max_value:
                max_value = prices[i]
                continue
            else:
                dp[i] = max_value - prices[i]
                if dp[i] >= best_value:
                    best_value = dp[i]

        return best_value
            


























        # dp = [0] * len(prices)
        # max_price = prices[-1]
        # profit = 0

        # for i in range(len(prices)-2, -1, -1):

        #     p1 = prices[i]
           
        #     if prices[i+1] >= max_price:
        #         max_price = prices[i+1]
        #     if max_price - p1 > profit:
        #         profit = max_price - p1
            

        # return profit


