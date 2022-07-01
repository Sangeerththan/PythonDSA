def binomialCoeff(n, k):
    C = [[0 for j in range(k + 1)]
         for i in range(n + 1)]

    for i in range(0, n + 1):
        for j in range(0, min(i, k) + 1):
            if (j == 0 or j == i):
                C[i][j] = 1
            else:
                C[i][j] = (C[i - 1][j - 1]
                           + C[i - 1][j])

    return C[n][k]

def lobb(n, m):
    return (((2 * m + 1) *
             binomialCoeff(2 * n, m + n))
            / (m + n + 1))

n = 5
m = 3
print(int(lobb(n, m)))
