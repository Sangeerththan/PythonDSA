def maximumSegments(n, a, b, c):
    dp = [-1] * (n + 10)
    dp[0] = 0
    for i in range(0, n):

        if (dp[i] != -1):

            # conditions
            if (i + a <= n):  # avoid buffer overflow
                dp[i + a] = max(dp[i] + 1,
                                dp[i + a])

            if (i + b <= n):  # avoid buffer overflow
                dp[i + b] = max(dp[i] + 1,
                                dp[i + b])

            if (i + c <= n):  # avoid buffer overflow
                dp[i + c] = max(dp[i] + 1,
                                dp[i + c])

    return dp[n]

n,a,b,c = 7,5,2,5
print(maximumSegments(n, a,
                      b, c))