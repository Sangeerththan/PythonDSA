def minTimeForWritingChars(N, insert,
                           remove, cpy):
    if N == 0:
        return 0
    if N == 1:
        return insert
    dp = [0] * (N + 1)
    dp[1] = insert
    for i in range(2, N + 1):
        if i % 2 == 0:
            dp[i] = min(dp[i - 1] + insert,
                        dp[i // 2] + cpy)
        else:
            dp[i] = min(dp[i - 1] + insert,
                        dp[(i + 1) // 2] +
                        cpy + remove)

    return dp[N]

if __name__ == "__main__":
    N = 9
    insert = 1
    remove = 2
    cpy = 1
    print(minTimeForWritingChars(N, insert,
                                 remove, cpy))
