MAX = 50


def solve(dp, a, low, high, turn):
    if (low == high):
        return a[low] * turn
    if (dp[low][high] != 0):
        return dp[low][high]
    dp[low][high] = max(a[low] * turn + solve(dp, a,
                                              low + 1, high, turn + 1),
                        a[high] * turn + solve(dp, a,
                                               low, high - 1, turn + 1));

    return dp[low][high]


if __name__ == "__main__":
    arr = [1, 3, 1, 5, 2]
    n = len(arr)

    dp = [[0 for x in range(MAX)]
          for y in range(MAX)]

    print(solve(dp, arr, 0, n - 1, 1))
