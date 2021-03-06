
import sys
sys.path.append("lib")

import unittest
from lists import UnorderedList
from lists import OrderedList

class UnorderedListTestCase(unittest.TestCase):  
    def setUp(self):
        self.mylist = UnorderedList()
        self.mylist.add(12)
        self.mylist.add(22)
        self.mylist.add(9)
        self.mylist.add(89)
        self.mylist.add(71)
        self.mylist.add(16)

    def test_length(self):
        self.assertEqual(self.mylist.length(),6)

    def test_search(self):
        self.assertEqual(self.mylist.search(12),True)
        self.assertEqual(self.mylist.search(3),False)

    def test_remove(self):
        self.mylist.remove(12)
        self.mylist.remove(11)
        self.assertEqual(self.mylist.search(12),False)
        self.assertEqual(self.mylist.search(11),False)
        self.assertEqual(self.mylist.length(),5)

    def test_toList(self):
        self.assertEqual(self.mylist.toList(),[16,71,89,9,22,12])


class OrderedListTestCase(unittest.TestCase):  
    def setUp(self):
        self.mylist = OrderedList()
        self.mylist.add(12)
        self.mylist.add(22)
        self.mylist.add(9)
        self.mylist.add(89)
        self.mylist.add(71)
        self.mylist.add(16)

    def test_length(self):
        self.assertEqual(self.mylist.length(),6)

    def test_search(self):
        self.assertEqual(self.mylist.search(89),True)
        self.assertEqual(self.mylist.search(8),False)

    def test_remove(self):
        self.mylist.remove(12)
        self.mylist.remove(11)
        self.assertEqual(self.mylist.search(12),False)
        self.assertEqual(self.mylist.search(11),False)
        self.assertEqual(self.mylist.length(),5)

    def test_toList(self):
        self.assertEqual(self.mylist.toList(),[9,12,16,22,71,89])



if __name__ == '__main__':
    unittest.main()
