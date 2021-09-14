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
    bribes = 0
    crowd = [i + 1 for i in range(len(q))]
    for i in range(len(q), 0, -1):
        if (crowd[i] != q[i]):
            bribes += 1
            crowd[i - 1], crowd[i] = crowd[i], crowd[i - 1]
            if crowd == q:
                break


if __name__ == '__main__':
    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        q = list(map(int, input().rstrip().split()))

        minimumBribes(q)
