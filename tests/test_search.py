import sys
sys.path.append("lib")

import unittest
from search import * 

class SearchTestCase(unittest.TestCase):  

    def setUp(self):
        self.testlist = [1,2,32,8,17,19,42,13,0]


    def test_sequentialSearch(self):
        self.assertEqual(sequentialSearch(self.testlist,3),False)
        self.assertEqual(sequentialSearch(self.testlist,13),True)



if __name__ == '__main__':
    unittest.main()

