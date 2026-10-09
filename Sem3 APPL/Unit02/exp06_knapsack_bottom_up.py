def knapsack(weights, values, capacity):
    n = len(weights)
    dp = [[-1 for j in range(capacity + 1)] for i in range(n + 1)]

    def solve(i, w):
        if i == 0 or w == 0:
            return 0

        if dp[i][w] != -1:
            return dp[i][w]

        if weights[i - 1] <= w:
            dp[i][w] = max(
                values[i - 1] + solve(i - 1, w - weights[i - 1]),
                solve(i - 1, w)
            )
        else:
            dp[i][w] = solve(i - 1, w)

        return dp[i][w]

    return solve(n, capacity)


weights = [1, 3, 4, 5]
values = [1, 4, 5, 7]
capacity = 7

print("Maximum value:", knapsack(weights, values, capacity))