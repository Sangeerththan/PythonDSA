import numpy as np

def countEndless(input_mat, n):
    row = np.zeros((n, n))
    col = np.zeros((n, n))
    for j in range(n):
        isEndless = 1
        for i in range(n - 1, -1, -1):
            if (input_mat[i][j] == 0):
                isEndless = 0
            col[i][j] = isEndless
    for i in range(n):
        isEndless = 1
        for j in range(n - 1, -1, -1):
            if (input_mat[i][j] == 0):
                isEndless = 0
            row[i][j] = isEndless
    ans = 0
    for i in range(n):
        for j in range(1, n):
            if (row[i][j] and col[i][j]):
                ans += 1
    return ans

if __name__ == "__main__":
    input_mat = [[1, 0, 1, 1],
                 [0, 1, 1, 1],
                 [1, 1, 1, 1],
                 [0, 1, 1, 0]]
    n = 4
    print(countEndless(input_mat, n))
