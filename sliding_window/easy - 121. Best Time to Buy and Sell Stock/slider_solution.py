"""
You are given an array prices where prices[i] is the price of a given stock on the ith day.
You want to maximize your profit by choosing a single day to buy one stock
and choosing a different day in the future to sell that stock.
Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

Example 1:
Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.

Example 2:
Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.
"""

def maxProfit(prices):
    # iterate through array and find a) lowest buying price b) the highest selling price and calc the difference

    # best buying day initialized as the first day/value in array
    best_buy = prices[0]
    max_profit = 0

    # range from 1, not 0 because we cannot sell on the first day, we do not have anything to sell
    for i in range(1, len(prices)):
        # calc possible profit
        profit = prices[i] - best_buy

        # if new best profit found
        if profit > max_profit:
            max_profit = profit

        # if new best buying day found
        if prices[i] < best_buy:
            best_buy = prices[i]

    return max_profit

print(maxProfit([7,1,5,3,6,4]))
print(maxProfit([7,6,4,3,1]))
print(maxProfit([8, 9, 3, 6, 1, 2]))
