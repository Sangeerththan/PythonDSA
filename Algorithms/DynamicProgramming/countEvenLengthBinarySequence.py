def count_seq(n):
    nCr = 1
    res = 1
    for r in range(1, n + 1):
        nCr = (nCr * (n + 1 - r)) / r;

        res += nCr * nCr;

    return res;

n = 2
print("Count of sequences is"),
print(int(count_seq(n)))
