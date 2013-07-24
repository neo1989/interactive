
import sys
sys.path.append("lib");

import unittest
from lists import UnorderedList

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
        self.mylist.remove(71)
        self.mylist.remove(11)
        self.assertEqual(self.mylist.search(71),False)
        self.assertEqual(self.mylist.search(11),False)
        self.assertEqual(self.mylist.length(),5)

if __name__ == '__main__':
    unittest.main()




