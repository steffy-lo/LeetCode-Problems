"""
This DP solution is able to give the buy and sell index, but is less efficient and not required for the problem.
"""
def dp_solution_1(prices):
    # initialization
    max_so_far = [[0 for j in range(len(prices))] for i in range(len(prices))]

    max_profit = 0

    # buy index = i
    # sell index = j
    for i in range(len(prices)):
        for j in range(i, len(prices)):
            profit = prices[j] - prices[i]
            if profit > max_so_far[i][j-1]:
                max_so_far[i][j] = profit
            else:
                max_so_far[i][j] = max_so_far[i][j-1]
            max_profit = max(max_so_far[i][j], max_profit)

    return max_profit


"""
Our DP Solution.
"""
def dp_solution_2(prices):
    if len(prices) == 0:
        return 0

    # initialization
    max_profit = [0 for i in range(len(prices))]
    min_price = prices[0]

    for i in range(1, len(prices)):
        if prices[i] < min_price:
            min_price = prices[i]

        max_profit[i] = max(prices[i] - min_price, max_profit[i - 1])

    return max_profit[len(prices) - 1]


"""
Is this a DP Solution? One might argue that it is not...
"""
def main(prices):
    max_profit = 0
    buy = prices[0]

    for i in range(1, len(prices)):
        buy = min(buy, prices[i])
        max_profit = max(max_profit, prices[i]-buy)

    return max_profit


if __name__ == "__main__":
    print(main([7, 1, 5, 3, 6, 4]))
    print(dp_solution_1([7, 1, 5, 3, 6, 4]))
    print(dp_solution_2([7, 1, 5, 3, 6, 4]))

