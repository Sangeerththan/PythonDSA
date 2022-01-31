def numberOfPaths(m, n):
    for i in range(n, (m + n - 1)):
        path *= i;
        path //= (i - n + 1);
    return path;
print(numberOfPaths(3, 3));