#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumSwaps function below.
def minimumSwaps(arr):
    n = len(arr)
    swaps = 0
    i = 0
    while i < n-1:
        if arr[i] == i+1:
            continue
        arr[i],arr[arr[i]-1] = arr[arr[i]-1], arr[i]
        swaps+=1
        i+=1
    return swaps-1
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = minimumSwaps(arr)

    fptr.write(str(res) + '\n')

    fptr.close()