# time -> o(n)
# mem -> o(1)

def maxProfit(prices):
    l, r = 0, 1
    maxP = 0

    while r < len(prices):
        if prices[l] < prices[r]:
            profit = prices[r] - prices[l]
            maxP = max(profit, maxP)
        else:
            l = r
        r += 1
    return maxP



prices = [7,1,5,3,6,4]
result = maxProfit(prices)
print(f"result: {result}")
