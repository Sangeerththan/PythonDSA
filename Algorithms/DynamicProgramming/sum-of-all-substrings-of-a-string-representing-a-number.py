def sumOfSubstrings(num):
    n = len(num)
    prev = int(num[0])
    res = prev
    current = 0
    for i in range(1, n):
        numi = int(num[i])
        current = (i + 1) * numi + 10 * prev
        res += current
        prev = current

    return res


num = "1234"
print(sumOfSubstrings(num))
