def maxSubArraySumRepeated(a, n, k):
    max_so_far = -2147483648
    max_ending_here = 0

    for i in range(n * k):
        max_ending_here = max_ending_here + a[i % n]

        if (max_so_far < max_ending_here):
            max_so_far = max_ending_here

        if (max_ending_here < 0):
            max_ending_here = 0

    return max_so_far

a = [10, 20, -30, -1]
n = len(a)
k = 3

print("Maximum contiguous sum is ",
      maxSubArraySumRepeated(a, n, k))
