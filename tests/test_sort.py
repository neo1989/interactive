import sys
sys.path.append("lib")

import unittest
from sort import * 
from lists import * 


class bubbleSortTestCase(unittest.TestCase):  

    def setUp(self):
        mylist = UnorderedList()
        mylist.add(12)
        mylist.add(22)
        mylist.add(9)
        mylist.add(89)
        mylist.add(71)
        mylist.add(16)

        self.testlist = mylist.toList()
    
    def test_sort(self):
        self.assertEqual(bubbleSort(self.testlist),[9,12,16,22,71,89])

class selectSortTestCase(unittest.TestCase):

    def setUp(self):
        mylist = UnorderedList()
        mylist.add(12)
        mylist.add(22)
        mylist.add(9)
        mylist.add(89)
        mylist.add(71)
        mylist.add(16)

        self.testlist = mylist.toList()

    def test_sort(self):
        self.assertEqual(selectSort(self.testlist),[9,12,16,22,71,89])

class insertionSortTestCase(unittest.TestCase):

    def setUp(self):
        mylist = UnorderedList()
        mylist.add(12)
        mylist.add(22)
        mylist.add(9)
        mylist.add(89)
        mylist.add(71)
        mylist.add(16)

        self.testlist = mylist.toList()

    def test_sort(self):
        self.assertEqual(insertionSort(self.testlist),[9,12,16,22,71,89])





if __name__ == "__main__":
    unittest.main()


