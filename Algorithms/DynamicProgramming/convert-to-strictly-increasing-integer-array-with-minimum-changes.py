def minRemove(arr, n):
    LIS = [0 for i in range(n)]
    len = 0
    for i in range(n):
        LIS[i] = 1
    for i in range(1, n):
        for j in range(i):
            if (arr[i] > arr[j] and (i - j) <= (arr[i] - arr[j])):
                LIS[i] = max(LIS[i], LIS[j] + 1)
        len = max(len, LIS[i])
    return (n - len)

arr = [1, 2, 6, 5, 4]
n = len(arr)
print(minRemove(arr, n))
