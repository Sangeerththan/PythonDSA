def countWays(arr, m, N):
    count = [0 for i in range(N + 1)]
    count[0] = 1
    for i in range(1, N + 1):
        for j in range(m):
            if i >= arr[j]:
                count[i] += count[i - arr[j]]
    return count[N]


arr = [1, 5, 6]
m = len(arr)
N = 7
print('Total number of ways = ',
      countWays(arr, m, N))
