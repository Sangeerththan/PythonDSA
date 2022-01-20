def numberOfWays(x):
    dp = []
    dp.append(1)
    dp.append(1)
    for i in range(2, x + 1):
        dp.append(dp[i - 1] + (i - 1) * dp[i - 2])
    return (dp[x])

x = 3
print(numberOfWays(x))