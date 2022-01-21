def binomialCoeff(n, k):
    C = [0] * (k + 1)
    C[0] = 1
    for i in range(1, n + 1):

        j = min(i, k)
        while (j > 0):
            C[j] = C[j] + C[j - 1]
            j -= 1

    return C[k]
n = 3
m = 2
print("Number of Paths:", binomialCoeff(n + m, n))