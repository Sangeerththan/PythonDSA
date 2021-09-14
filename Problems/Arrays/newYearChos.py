#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'minimumBribes' function below.
#
# The function accepts INTEGER_ARRAY q as parameter.
#

def minimumBribes(q):
    # Write your code here
    bribe = 0
    n = len(q)
    for i in range(n - 1, -1, -1):
        if q[i] - (i + 1) > 2:
            print("Too chaotic")
            return
        j = max(0, q[i] - 2)
        while j < i:
            if q[j] > q[i]:
                bribe += 1
            j += 1
    print(bribe)


if __name__ == '__main__':
    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        q = list(map(int, input().rstrip().split()))

        minimumBribes(q)
