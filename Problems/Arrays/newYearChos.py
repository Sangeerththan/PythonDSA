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
    for i in range(len(q) - 1):
        if (q[i] > q[i + 1]):
            succesive_bribe = q[i] - q[i + 1]
            if succesive_bribe > 2:
                print("Too chaotic")
                return
            else:
                bribe += succesive_bribe
    print(bribe)


if __name__ == '__main__':
    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        q = list(map(int, input().rstrip().split()))

        minimumBribes(q)
