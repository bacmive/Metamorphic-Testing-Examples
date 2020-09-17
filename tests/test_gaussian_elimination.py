##########################################################################
# File name: test_gaussian_elimination.py
# Author: tam sei kwan
# eMail:1228150491@qq.com
# Created Time: 2020年09月16日 星期三 09时08分57秒
##########################################################################
#!/usr/bin/env python
# coding=utf-8
import sys
sys.path.append("..")
from programs import gaussian_elimination
import numpy as np
import unittest
import random

def swap_rows(A, i, j):
    A[i], A[j] = A[j], A[i]
    return A

def swap_cols(A, i, j):
    if len(np.array(A).shape) != 2:
        return A
    n = len(A[0])
    if i<0 or j<0 or i>=n or j>=n:
        return A

    for k in range(len(A)):
        A[k][i], A[k][j] = A[k][j], A[k][i]

    return A

class MR1(unittest.TestCase):
    '''
    the source test case is (A,b), accordingly the output is x
    we construct the follow-up test case (A',b') by swap the row i and row j
    in both A and b, where i,j chose by random.sample
    '''
    def __init__(self, A=None, b=None):
        super().__init__('test_mr')
        self.A =A
        self.b =b

    def test_mr(self):
        x = gaussian_elimination(self.A, self.b)
        
        # construct the follow-up test case
        i, j = random.sample(range(len(self.A)), 2)
        A1 = swap_rows(self.A, i, j)
        b1 = swap_rows(self.b, i, j)
        x1 = gaussian_elimination(A1, b1)

        self.assertAlmostEqual(x,x1)
    
class MR2(unittest.TestCase):
    '''
    Just like the MR1 above
    Here we construct the follow-up test case by swap two colomns in A
    the output should be the source test case's output with two cols swaped
    '''
    def __init__(self, A=None, b=None):
        super().__init__('test_mr')
        self.A =A
        self.b =b

    def test_mr(self):
        x = gaussian_elimination(self.A, self.b)
        
        # construct the follow-up test case
        i, j = random.sample(range(len(self.A)), 2)
        A1 = swap_cols(self.A, i, j)
        b1 = self.b
        x1 = gaussian_elimination(A1,b1)
        x1 = swap_rows(x1, i, j)
        self.assertAlmostEqual(x1,x)

def load_tests():
    suite = unittest.TestSuite()
    
    A =[
        [1,2,3],
        [2,2,3],
        [3,3,3]
    ]
    b=[1,1,1]

    suite.addTest(MR1(A, b))
    suite.addTest(MR2(A, b))
    return suite

if __name__ == "__main__":
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(load_tests())
