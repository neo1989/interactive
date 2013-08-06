import sys
sys.path.append("lib")

import unittest
from search import * 
from lists import * 

class sequentialSearchTestCase(unittest.TestCase):  

    def setUp(self):
        mylist = UnorderedList()
        mylist.add(12)
        mylist.add(22)
        mylist.add(9)
        mylist.add(89)
        mylist.add(71)
        mylist.add(16)

        self.testlist = mylist.toList()

    def test_sequentialSearch(self):
        self.assertEqual(sequentialSearch(self.testlist,3),False)
        self.assertEqual(sequentialSearch(self.testlist,16),True)


class orderedSequentialSearchTestCase(unittest.TestCase):  

    def setUp(self):
        mylist = OrderedList()
        mylist.add(12)
        mylist.add(22)
        mylist.add(9)
        mylist.add(89)
        mylist.add(71)
        mylist.add(16)

        self.testlist = mylist.toList()

    def test_sequentialSearch(self):
        self.assertEqual(sequentialSearch(self.testlist,3),False)
        self.assertEqual(sequentialSearch(self.testlist,16),True)


if __name__ == '__main__':
    unittest.main()

