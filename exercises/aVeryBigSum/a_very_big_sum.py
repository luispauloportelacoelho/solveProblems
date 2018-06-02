#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the aVeryBigSum function below.
def aVeryBigSum(ar):
    size_ar = len(ar)

    sum = 0

    for i in range(size_ar):
        sum += ar[i]

    return sum


print(aVeryBigSum([5, 2, 3, 5]))

'''if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ar_count = int(input())

    ar = list(map(int, input().rstrip().split()))

    ar = [1, 2, 3, 4]

    result = aVeryBigSum(ar)

    fptr.write(str(result) + '\n')

    fptr.close()'''
