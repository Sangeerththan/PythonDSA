def binomial_coefficient(n, k):
    if k > n:
        return 0
    if k == 0 or k == n:
        return 1
    return binomial_coefficient(n - 1, k - 1) + binomial_coefficient(n - 1, k)


n = 10
k = 2
print("Value of C(%d,%d) is (%d)" % (n, k, binomial_coefficient(n, k)))
