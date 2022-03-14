def find_prob(N, P):
    dp = [0] * (n + 1)
    dp[0] = 1
    dp[1] = 0
    dp[2] = P
    dp[3] = 1 - P
    for i in range(4, N + 1):
        dp[i] = (P) * dp[i - 2] + (1 - P) * dp[i - 3]
    return dp[N]

n = 5
p = 0.2
print(round(find_prob(n, p), 2))
