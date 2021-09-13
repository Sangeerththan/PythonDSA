def iteratingDifference(n, a, b):
    for i in range(n):
        if a > b:
            a = a - b
        elif b > a:
            b = b - a
        elif a == b:
            return 0
    return (a, b)


print(iteratingDifference(9, 2437, 875))
