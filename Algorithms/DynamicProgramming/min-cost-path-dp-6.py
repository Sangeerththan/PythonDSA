def minCost(cost, row, col):
    for i in range(1, row):
        cost[i][0] += cost[i - 1][0]
    for j in range(1, col):
        cost[0][j] += cost[0][j - 1]
    for i in range(1, row):
        for j in range(1, col):
            cost[i][j] += (min(cost[i - 1][j - 1],
                               min(cost[i - 1][j],
                                   cost[i][j - 1])))

    return cost[row - 1][col - 1]

if __name__ == '__main__':
    row = 3
    col = 3

    cost = [[1, 2, 3],
            [4, 8, 2],
            [1, 5, 3]]
    print(minCost(cost, row, col))
