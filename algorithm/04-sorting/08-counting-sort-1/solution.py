#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countingSort function below.


def countingSort(arr):
    n = len(arr)
    result = [0] * 100
    for elm in arr:
        result[elm] += 1
    return result


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = countingSort(arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
