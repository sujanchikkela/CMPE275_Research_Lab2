# defining the max profit alogorithm in pure python to calculate best time to buy and sell stock.
def maxProfit(prices):
    max_profit = 0
    for i in range(len(prices) - 1):
        for j in range(i + 1, len(prices)):
            profit = prices[j] - prices[i]
            if profit > max_profit:
                max_profit = profit
        return max_profit
