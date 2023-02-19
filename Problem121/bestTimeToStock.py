prices = [7,2,2,5,14,3,2,1,4]
# maxProfit = 0
minValue = 10001
# maxValue = 0
# buy = -1
# sell = 0

profit = 0
for i in range(len(prices)):
    if(prices[i] < minValue):
        minValue = prices[i]
    if(prices[i] - minValue > profit):
        profit = prices[i] - minValue

# maxProfit = maxValue - minValue
# print(maxValue)
# print(minValue)
print(profit)

