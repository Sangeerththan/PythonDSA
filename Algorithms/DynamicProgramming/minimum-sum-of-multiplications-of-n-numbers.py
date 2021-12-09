import numpy as np
import sys
dp = np.zeros((1000, 1000))
def sum(a, i, j):
    ans = 0
    for m in range(i, j + 1):
        ans = (ans + a[m]) % 100

    return ans
def solve(a, i, j):
    if (i == j):
        return 0
    if (dp[i][j] != -1):
        return dp[i][j]
    dp[i][j] = sys.maxsize
    for k in range(i, j):
        dp[i][j] = min(dp[i][j], (solve(a, i, k) + solve(a, k + 1, j)
                                  + (sum(a, i, k) * sum(a, k + 1, j))))
    return dp[i][j]
def initialize(n):
    for i in range(n + 1):
        for j in range(n + 1):
            dp[i][j] = -1
if __name__ == "__main__":
    a = [40, 60, 20]
    n = len(a)
    initialize(n)
    print(int(solve(a, 0, n - 1)))
