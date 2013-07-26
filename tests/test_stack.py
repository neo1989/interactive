
import sys
sys.path.append("lib")

import unittest
from stack import Stack 

class StackTestCase(unittest.TestCase):

    def setUp(self):
        self.stack = Stack()

    def test_isEmpty(self):
        self.assertEqual(self.stack.isEmpty(),True)

    def test_pop(self):
        self.stack.push(1)
        self.stack.push('dog')
        self.assertEqual(self.stack.pop(),'dog')
        self.assertEqual(self.stack.size(),1)

    def test_peek(self):
        self.stack.push(1)
        self.stack.push('dog')
        self.assertEqual(self.stack.peek(),'dog')
        self.assertEqual(self.stack.size(),2)



if __name__ == '__main__':
    unittest.main()
