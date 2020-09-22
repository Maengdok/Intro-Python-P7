#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the aVeryBigSum function below.
def aVeryBigSum(ar):
    result = 0
    sumFirstElem = 0
    sumLastElem = 0

    for i in ar:
        list = ar[i]
        for j in list:
            getFirstElem = list[0]
            getlastElem = list[-1]

    sumFirstElem = sumFirstElem + getFirstElem
    sumLastElem = sumLastElem + getLastElem
    result = sumFirstElem + sumLastElem

    return(result)

if __name__ == '__main__':


    ar_count = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = aVeryBigSum(ar)

    print(result)
