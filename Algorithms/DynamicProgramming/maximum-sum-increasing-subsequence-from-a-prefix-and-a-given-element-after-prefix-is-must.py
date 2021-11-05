def pre_compute(a, n, index, k):
    # Base case
    if (index >= k):
        return -1
    dp = [0 for i in range(index)]
    for i in range(index):
        dp[i] = a[i]

    maxi = -float('inf')

    for i in range(index):
        if (a[i] >= a[k]):
            continue

        for j in range(i):
            if (a[i] > a[j]):
                dp[i] = dp[j] + a[i]
            maxi = max(maxi, dp[i])
    if (maxi == -float('inf')):
        return a[k]

    return maxi + a[k]

a = [1, 101, 2, 3, 100, 4, 5]
n = len(a)
index = 4
k = 6

print(pre_compute(a, n, index, k))