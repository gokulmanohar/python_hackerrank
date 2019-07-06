#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the compareTriplets function below.
def compareTriplets(a,b):
    x=0#alice
    y=0#bob
    for i in range(3):
        if a[i]>b[i]:
            x=x+1
        elif b[i]>a[i]:
            y=y+1
        else:
            x=x+0
            y=y+0
    z=[x,y]
    return(z)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    result = compareTriplets(a, b)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
