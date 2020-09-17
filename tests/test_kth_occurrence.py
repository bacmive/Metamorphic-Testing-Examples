import sys
sys.path.append("..")
from programs import kth_occurrence
import unittest
import random

class MR1(unittest.TestCase):
	'''
	when then output of program is -1,
	construct the follow-up test case by randomly choose an element A[r] in array
	that is (A[r], 1, A), which should return m, and m<=r
	'''
	def __init__(self, x=None, k= None, A=None):
		super().__init__('test_mr')
		self.x = x
		self.k = k
		self.A = A
	
	def test_mr(self):
		self.assertEqual(kth_occurrence(self.x, self.k, self.A, 0, len(self.A)-1), -1)
		r = int(random.random()*len(self.A))
		self.assertLessEqual(kth_occurrence(self.A[r], 1, self.A, 0, len(self.A)-1), r)

class MR2(unittest.TestCase):
	''' 
	when the overwriting error happen, the output of the program is p,
	and A[p] is overwrited with x
	construct the follow-up test case by choosing a y
	while y!=A[p-1], y!=A[p] and y!=A[p+1]
	two new test case: One is (y, 1, A[p..]), the other is (y, 1, A[p-1..p+1])
	they should all return -1
	'''
	def __init__(self, x=None, k=None, A=None):
		super().__init__('test_mr')
		self.x = x
		self.k = k
		self.A = A
	
	def test_mr(self):
		p = kth_occurrence(self.x, self.k, self.A, 0, len(self.A)-1)
		self.assertEqual(self.A[p], self.x)
		
		# One new test case
		y = self.A[p] + 1  
		left_bound = p
		right_bound = p
		if p > 0:
			y = self.A[p-1] + 1
			if y==self.A[p]:
				y = self.A[p] + 1
			left_bound = p - 1
		if p < len(self.A) - 1:
			y = self.A[p] + 1
			if y == self.A[p+1]:
				y = self.A[p+1] + 1
			right_bound = p +1
		self.assertEqual(kth_occurrence(y, 1, self.A, p, p), -1)
		self.assertEqual(kth_occurrence(y, 1, self.A, left_bound, right_bound), -1)

class MR3(unittest.TestCase):
	'''
		overwriting error
		the program starts overwriting the subsequent array entries 
		only after it hits the first occurrence of x
		construct the follow-up case (x, 2, A[r-1, len(A)-1])
		where x is the source-test-case's input key
		r:starting from A[p] until an element A[r]!=x
		the follow-up case result m is -1 or greater than r
	'''
	def __init__(self, x=None, k=None, A=None):
		super().__init__('test_mr')
		self.x = x
		self.k = k
		self.A = A
	
	def test_mr(self):
		p = kth_occurrence(self.x, self.k, self.A, 0, len(self.A)-1)
		self.assertEqual(self.A[p], self.x)
		
		r = p
		for i in range(p, len(self.A)):
			if self.A[i] != self.x:
				r = i
				break
		
		m = kth_occurrence(self.x, 2, self.A, r-1, len(self.A)-1)
		if m == -1:
			self.skipTest("skip due to success")
		else:
			self.assertGreater(m, r)
		
		
def load_tests():
	suite = unittest.TestSuite()
	A = [3, 1, 2, 1, 0, 0, 0, 1, 3, 3, 2, 2]
	x1 = 0
	k1 = 4
	x2 = 0
	k2 = 3
	x3 = 1
	k3 = 3
	
	suite.addTest(MR1(x1, k1, A))
	suite.addTest(MR2(x2, k2, A))
	suite.addTest(MR3(x3, k3, A))
	return suite
	
if __name__ == '__main__':
	runner = unittest.TextTestRunner(verbosity=2)
	runner.run(load_tests())
