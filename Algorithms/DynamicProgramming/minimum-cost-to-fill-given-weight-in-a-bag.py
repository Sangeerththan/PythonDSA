import sys

def minCost(cost, n):
    dp = [0 for i in range(n + 1)]
    for i in range(1, n + 1):
        min_cost = sys.maxsize
        for j in range(i):
            if j < len(cost) and cost[j] != -1:
                min_cost = min(min_cost,
                               cost[j] + dp[i - j - 1])
        dp[i] = min_cost
    return dp[n]

cost = [10, -1, -1, -1, -1]
W = len(cost)

print(minCost(cost, W))
