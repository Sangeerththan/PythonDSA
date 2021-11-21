MAX = 1000


def maxCost(mat, N):
    dp = [[0 for i in range(N)] for j in range(N)]
    dp[0][0] = mat[0][0]
    for i in range(1, N):
        dp[i][0] = mat[i][0] + dp[i - 1][0]
    for i in range(1, N):
        for j in range(1, min(i + 1, N)):
            dp[i][j] = mat[i][j] + \
                       max(dp[i - 1][j - 1],
                           dp[i - 1][j])
    result = 0
    for i in range(N):
        if (result < dp[N - 1][i]):
            result = dp[N - 1][i]
    return result
mat = [[4, 1, 5, 6, 1],
       [2, 9, 2, 11, 10],
       [15, 1, 3, 15, 2],
       [16, 92, 41, 4, 3],
       [8, 142, 6, 4, 8]]

N = 5
print('Maximum Path Sum :', maxCost(mat, N))