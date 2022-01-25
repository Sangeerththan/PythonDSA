def prCountDP(dist):
    ways = [0] * 3
    n = dist
    ways[0] = 1
    ways[1] = 1
    ways[2] = 2
    for i in range(3, n + 1):
        ways[i % 3] = ways[(i - 1) % 3] + ways[(i - 2) % 3] + ways[(i - 3) % 3]

    return ways[n % 3]
dist = 4
print(prCountDP(dist))
