def uniquePathsWithObstacles(A):
    paths = [[0] * len(A[0]) for i in A]
    if A[0][0] == 0:
        paths[0][0] = 1
    for i in range(1, len(A)):
        if A[i][0] == 0:
            paths[i][0] = paths[i - 1][0]
    for j in range(1, len(A[0])):
        if A[0][j] == 0:
            paths[0][j] = paths[0][j - 1]
    for i in range(1, len(A)):
        for j in range(1, len(A[0])):
            if A[i][j] == 0:
                paths[i][j] = paths[i - 1][j] + paths[i][j - 1]
    return paths[-1][-1]


A = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
print(uniquePathsWithObstacles(A))
