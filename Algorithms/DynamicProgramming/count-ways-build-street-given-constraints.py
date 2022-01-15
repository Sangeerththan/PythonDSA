def countways(n):
    A = [0 for i in range(n + 2)]
    A[0] = 1
    A[1] = 3
    A[2] = 7
    for i in range(2, n + 1):
        A[i] = 2 * A[i - 1] + A[i - 2]

    return A[n]
n = 5
print(countways(5))
