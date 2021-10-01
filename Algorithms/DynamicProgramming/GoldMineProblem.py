MAX = 100


def get_max_gold(gold, m, n):
    gold_table = [[0 for i in range(n)]
                  for j in range(m)]

    for col in range(n - 1, -1, -1):
        for row in range(m):
            if col == n - 1:
                right = 0
            else:
                right = gold_table[row][col + 1]
            if row == 0 or col == n - 1:
                right_up = 0
            else:
                right_up = gold_table[row - 1][col + 1]
            if row == m - 1 or col == n - 1:
                right_down = 0
            else:
                right_down = gold_table[row + 1][col + 1]
            gold_table[row][col] = gold[row][col] + max(right, right_up, right_down)
    res = gold_table[0][0]
    for i in range(1, m):
        res = max(res, gold_table[i][0])

    return res


gold = [[1, 3, 1, 5],
        [2, 2, 4, 1],
        [5, 0, 2, 3],
        [0, 6, 1, 2]]

m = 4
n = 4

print(get_max_gold(gold, m, n))
