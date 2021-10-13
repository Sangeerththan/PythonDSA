def nswp(n):
    if (n < 2): return 1
    a, b = 1, 1
    for i in range(2, n + 1):
        c = 2 * b + a
        a = b
        b = c
    return b


n = 3
print(nswp(n))
