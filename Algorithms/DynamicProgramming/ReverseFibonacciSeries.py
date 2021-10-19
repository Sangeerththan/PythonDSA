def reverseFibonacci(n):
    a = [0] * n
    a[0] = 0
    a[1] = 1

    for i in range(2, n):
        a[i] = a[i - 2] + a[i - 1]

    for i in range(n - 1, -1, -1):
        print(a[i], end=" ")

n = 5
reverseFibonacci(n)
