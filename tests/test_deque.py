
import sys
sys.path.append("lib");

import unittest
from deque import Deque 


class DequeTestCase(unittest.TestCase):  

    def setUp(self):
        self.d = Deque()

    def test_isEmpty(self):
        self.assertEqual(self.d.isEmpty(),True)
    
    def test_front(self):
        self.d.addFront(1)
        self.d.addFront('a')
        self.assertEqual(self.d.removeFront(),'a')
        self.assertEqual(self.d.removeFront(),1)

    def test_rear(self):
        self.d.addRear(1)
        self.d.addRear('a')
        self.assertEqual(self.d.removeRear(),'a')
        self.assertEqual(self.d.removeRear(),1)

    def test_queue(self):
        self.d.addFront(1)
        self.assertEqual(self.d.removeRear(),1)
        self.d.addRear('a')
        self.assertEqual(self.d.removeFront(),'a')


if __name__ == '__main__':
    unittest.main()

