def maxSum(grid, n):
    incl = max(grid[0][0], grid[1][0])
    excl = 0
    for i in range(1, n):
        excl_new = max(excl, incl)
        incl = excl + max(grid[0][i], grid[1][i])
        excl = excl_new
    return max(excl, incl)


if __name__ == "__main__":
    grid = [[1, 2, 3, 4, 5],
            [6, 7, 8, 9, 10]]
    n = 5
    print(maxSum(grid, n))
