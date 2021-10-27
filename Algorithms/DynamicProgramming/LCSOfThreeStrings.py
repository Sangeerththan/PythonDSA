X = "AGGT12"
Y = "12TXAYB"
Z = "12XBA"

dp = [[[-1 for i in range(100)]
       for j in range(100)]
      for k in range(100)]

def lcsOf3(i, j, k):
    if (i == -1 or j == -1 or k == -1):
        return 0

    if (dp[i][j][k] != -1):
        return dp[i][j][k]

    if (X[i] == Y[j] and Y[j] == Z[k]):
        dp[i][j][k] = 1 + lcsOf3(i - 1,
                                 j - 1, k - 1)
        return dp[i][j][k]

    else:
        dp[i][j][k] = max(max(lcsOf3(i - 1, j, k),
                              lcsOf3(i, j - 1, k)),
                          lcsOf3(i, j, k - 1))

        return dp[i][j][k]

if __name__ == "__main__":
    m = len(X)
    n = len(Y)
    o = len(Z)

    print("Length of LCS is",
          lcsOf3(m - 1, n - 1, o - 1))
