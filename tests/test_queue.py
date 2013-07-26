import sys
sys.path.append("lib")

import unittest
from queue import Queue

class QueueTestCase(unittest.TestCase):
    def setUp(self):
        self.queue = Queue()

    def test_isEmpty(self):
        self.assertEqual(self.queue.isEmpty(),True)

    def test_queue(self):
        self.queue.enqueue(12)
        self.queue.enqueue('queue')
        self.queue.enqueue('end')
        self.assertEqual(self.queue.size(),3)
        self.assertEqual(self.queue.dequeue(),12)
        self.assertEqual(self.queue.dequeue(),'queue')
        self.assertEqual(self.queue.size(),1)



if __name__ == "__main__":
    unittest.main()
