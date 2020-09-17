import sys
sys.path.append("..")
from programs import shortest_path
import unittest
import random

class MR1(unittest.TestCase):
    '''
    the source test case is (x,y,G), the output of the program is p, 
    we construct the follow-up case (y,x,G), the follow-up output should be the same
    '''
    def __init__(self, start=None, end=None, graph=None):
        super().__init__('test_mr')
        self.start = start
        self.end = end
        self.graph = graph

    def test_mr(self):
        val, path = shortest_path(self.start, self.end, self.graph)
        val2, path2 = shortest_path(self.end, self.start, self.graph)

        self.assertEqual(val, val2)


class MR2(unittest.TestCase):
    '''
    the source test case is (x, y, G), 
    and it's shortest path of output is "x, v1, v2...y"
    we construct the follow-up test case (x, vi, G) and (vi, y, G),
    where vi satisfies that 1<=i<=k
    '''
    def __init__(self, start=None, end=None, graph=None):
        super().__init__('test_mr')
        self.start = start
        self.end = end
        self.graph = graph

    def test_mr(self):
        val, path = shortest_path(self.start, self.end, self.graph)

        # randomly choose one node in the middle
        vi = path[int(random.random()*len(path))]
        val1, path1 = shortest_path(self.start, vi, self.graph)
        val2, path2 = shortest_path(vi, self.end, self.graph)

        self.assertEqual(val, val1+val2)

def load_tests():
    suite = unittest.TestSuite()

    G = [
        [0, 10, 20, 30],
        [10, 0, 15, 18],
        [20, 15, 0, 6],
        [30, 18, 6, 0]
    ]
    suite.addTest(MR1(1,4,G))
    suite.addTest(MR2(2,3,G))
    return suite

if __name__ == '__main__':
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(load_tests())
    
