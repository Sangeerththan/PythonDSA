def countWays(n):
    a = 1
    b = 2
    c = 4
    d = 0
    if (n == 0 or n == 1 or n == 2):
        return n
    if (n == 3):
        return c

    for i in range(4, n + 1):
        d = c + b + a
        a = b
        b = c
        c = d
    return d

n = 4
print(countWays(n))
