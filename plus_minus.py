#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the plusMinus function below.
def plusMinus(arr):
    posi=0
    neg=0
    zer=0
    for i in range(len(arr)):
        if arr[i]>0:
            posi+=1
        elif arr[i]<0:
            neg+=1
        else:
            zer+=1
    n=len(arr)
    #print ("",end="") 
    print (posi/n)
    #print ("",end="") 
    print (neg/n)
    #print ("",end="") 
    print (zer/n) 

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
