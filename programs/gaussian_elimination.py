##########################################################################
# File name: gaussian_elimination.py
# Author: tam sei kwan
# eMail:1228150491@qq.com
# Created Time: 2020年09月16日 星期三 08时36分25秒
##########################################################################
#!/usr/bin/env python
# coding=utf-8
import numpy as np

def gaussian_elimination(A, b):
    n = len(A)
    for i in range(1,n):
        for j in range(i, n):
            delta = A[j][i-1]/( A[i-1][i-1] + 1e-9)
            for k in range(i-1, n):
                A[j][k] = A[j][k] - A[i-1][k]*delta
            b[j] = b[j]-b[i-1]*delta
    b[n-1] = b[n-1]/( A[n-1][n-1] + 1e-9)
    for i in range(n-2, -1, -1):
        for j in range(n-1, i, -1):
            b[i] = b[i] - A[i][j]*b[j]
        b[i] = b[i]/( A[i][i] + 1e-9 )

    return b

if __name__ == '__main__':
    A = [
        [1,2,3],
        [2,2,3],
        [3,3,3]
    ]

    b = [1,1,1]

    print(gaussian_elimination(A, b))
