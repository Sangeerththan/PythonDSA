# Recursive Python3 program for
# coin change problem.

# Returns the count of ways we can sum
# S[0...m-1] coins to get sum n
def count(S, m, n):
    if n == 0:
        return 1
    if n < 0:
        return 0;
    if m <= 0 and n >= 1:
        return 0
    return count(S, m - 1, n) + count(S, m, n - S[m - 1]);


arr = [1, 2, 3]
m = len(arr)
print(count(arr, m, 4))
