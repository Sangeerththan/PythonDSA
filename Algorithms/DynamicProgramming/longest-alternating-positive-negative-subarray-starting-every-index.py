def longestAlternating(arr, n):
    count = [None] * n
    count[n - 1] = 1
    i = n - 2
    while i >= 0:
        if (arr[i] * arr[i + 1] < 0):
            count[i] = count[i + 1] + 1
        else:
            count[i] = 1;
        i = i - 1
    i = 0
    while i < n:
        print(count[i], end=" ")
        i = i + 1


a = [-5, -1, -1, 2, -2, -3]
n = len(a)
longestAlternating(a, n);
