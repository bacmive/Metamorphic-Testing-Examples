import sys
sys.path.append("..")
from programs import binary_search
import unittest
import random


class MR1(unittest.TestCase):
	'''
	when k=-1, it represents that x isn't in the array A
	there might be possible errors in the program
	then randomly choose one elements A[p] in the array A of input
	'''
	def __init__(self, name, A=None, x=None):
		super().__init__(name)
		self.A = A 
		self.x = x
		
	def test_mr(self):
		# ensure that x is not in the array A
		self.assertEqual(binary_search(self.x, self.A, 0, len(self.A)-1), -1) 
		# randomly generate new test case
		p = int(random.random()*len(self.A))
		y = self.A[p]
		self.assertEqual(binary_search(y, self.A, 0, len(self.A)-1), p)


class MR2(unittest.TestCase):
	'''
	when k>=0 and A[k-1]<A[k]=x<A[k+1]
	overwriting errors could happen, and x is accidently inserted into the array A
	then choose a value y which is A[k-1]<y!=x<A[k+1],
	construct the new test case (y, A, 0, len(A)-1)
	'''
	def __init__(self, name, A=None, x=None):
		super().__init__(name)
		self.A = A
		self.x = x
	
	def test_mr(self):
		# ensure that the test case(x, A, 0, len(A)-1) satisfy the conditions
		k = binary_search(self.x, self.A, 0, len(self.A)-1)
		self.assertEqual(self.x, self.A[k])
		if k-1 >= 0:
			self.assertLess(self.A[k-1], self.A[k])
		if k+1 <= len(self.A)-1:
			self.assertLess(self.A[k], self.A[k+1])
		
		for i in range(0,k+1):
			self.A[i] -=1
			
		self.assertEqual(binary_search(self.x, self.A,0,len(self.A)-1), -1)
		
		
class MR3(unittest.TestCase):
	'''
	when k>=0 and A[k]=x, there still possibly be splitting error,
	construct new two test case (A[k-1], A, 0, len(A)-1) and (A[k+1], A, 0, len(A)-1)
	return k-1 and k+1 respectively
	'''
	def __init__(self, name, A=None, x=None):
		super().__init__(name)
		self.A = A
		self.x = x
	
	def test_mr(self):
		k = binary_search(self.x, self.A, 0, len(self.A)-1)
		if k-1 >= 0:
			self.assertEqual(binary_search(self.A[k-1], self.A, 0, len(self.A)-1), k-1)
		if k+1 <= len(self.A)-1:
			self.assertEqual(binary_search(self.A[k+1], self.A, 0, len(self.A)-1), k+1)

def load_tests():
	suite = unittest.TestSuite()
	A = [4, 6, 10, 15, 18, 25, 40]
	key1 = 27
	key2 = 25
	key3 = 25
	
	suite.addTest(MR1('test_mr', A, key1))
	suite.addTest(MR2('test_mr', A, key2))
	suite.addTest(MR3('test_mr', A, key3))
	
	return suite

if __name__ == '__main__':
	runner = unittest.TextTestRunner(verbosity=2)
	runner.run(load_tests())
	
