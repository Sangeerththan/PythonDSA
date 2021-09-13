#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'repeatedString' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. STRING s
#  2. LONG_INTEGER n
#

def repeatedString(s, n):
    # Write your code here
    count = 0;
    occurence = 0
    if set(s) == {'a'}:
        return n
    else:
        for character in s:
            if (character == 'a'):
                count += 1
        print(count)
        occurence = count * (n // len(s))
        for character in s[-(n % len(s)):]:
            if (character == 'a'):
                count += 1
                occurence += 1
        return occurence


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input().strip())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()