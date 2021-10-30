def maxSumIS(arr, n):
    maxi = 0
    msis = [0 for x in range(n)]

    for i in range(n):
        msis[i] = arr[i]

    for i in range(1, n):
        for j in range(i):
            if (arr[i] > arr[j] and
                    msis[i] < msis[j] + arr[i]):
                msis[i] = msis[j] + arr[i]

    # Pick maximum of
    # all msis values
    for i in range(n):
        if maxi < msis[i]:
            maxi = msis[i]

    return maxi


arr = [1, 101, 2, 3, 100, 4, 5]
n = len(arr)
print("Sum of maximum sum increasing " +
      "subsequence is " +
      str(maxSumIS(arr, n)))
