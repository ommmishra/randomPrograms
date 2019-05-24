#!/bin/python3

import os
import sys

#
# Complete the getTotalX function below.
#
def getTotalX(a, b):
    #
    # Write your code here.
    #
    a.sort()
    b.sort()
    c = []
    d = 0
    a1 = a[0]
    b1 = b[0]

    for x in range(a1,b1+1):
        for y in range(0,len(a)):
            if(x % a[y] == 0):
                d +=1
            else:
                d = 0
                break
        if(d == len(a)):
            c.append(x)
            d = 0
    d = 0 
    c1 = len(c)
    for x in range(0,len(c)):
        for y in range(0, len(b)):
            if(b[y] % c[x] == 0):
                continue
            else:
                c1 -= 1
                break
    return c1
        


if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    total = getTotalX(a, b)

    f.write(str(total) + '\n')

    f.close()