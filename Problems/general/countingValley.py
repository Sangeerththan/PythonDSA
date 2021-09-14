#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'countingValleys' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER steps
#  2. STRING path
#

def countingValleys(steps, path):
    # Write your code here
    valleys = 0
    downhill = 0
    uphill = 0
    inValley = False
    for i in range(steps):
        if path[i] == 'D':
            downhill += 1
            if downhill == uphill and downhill != 0:
                downhill = 0
                uphill = 0
                inValley = False
            if downhill > uphill and not inValley:
                valleys += 1
                inValley = True
        elif path[i] == 'U':
            uphill += 1
            if downhill == uphill and downhill != 0:
                downhill = 0
                uphill = 0
                inValley = False
    return valleys


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    steps = int(input().strip())

    path = input()

    result = countingValleys(steps, path)

    fptr.write(str(result) + '\n')

    fptr.close()