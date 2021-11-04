def maxLenSub(arr, n):
    mls = []
    max = 0
    for i in range(n):
        mls.append(1)
    for i in range(n):
        for j in range(i):
            if (abs(arr[i] - arr[j]) <= 1 and mls[i] < mls[j] + 1):
                mls[i] = mls[j] + 1
    for i in range(n):
        if (max < mls[i]):
            max = mls[i]
    return max

arr = [2, 5, 6, 3, 7, 6, 5, 8]
n = len(arr)
print("Maximum length subsequence = ", maxLenSub(arr, n))
