import numpy as np


def waysToArrange(N, K, k):
    C = np.zeros((N + 1, N + 1))
    for i in range(N + 1):
        for j in range(i + 1):
            if (j == 0 or j == i):
                C[i][j] = 1
            else:
                C[i][j] = (C[i - 1][j - 1] +
                           C[i - 1][j])
    dp = np.zeros((K + 1))
    count = 0
    dp[0] = 1
    for i in range(K):
        dp[i + 1] = (dp[i] * C[count + k[i] - 1][k[i] - 1])
        count += k[i]
    return dp[K]


if __name__ == "__main__":
    N = 4
    k = [2, 2]

    K = len(k)
    print(int(waysToArrange(N, K, k)))
