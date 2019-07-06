#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    l = len(arr[0])
    x=[]
    y=[]
    
    x= [arr[i][i] for i in range(l)] #primary
    y= [arr[l-1-i][i] for i in range(l-1,-1,-1)] #secondary
    
    x1=0
    y1=0
    for i in range (l):
        x1=x1+x[i]
        y1=y1+y[i]
    z=abs(x1-y1)
    return(z)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
