import unittest
from lab4 import PriorityQueue

if __name__ == "__main__":
  unittest.main()

class TestPriorityQueue(unittest.TestCase):

  def test_enqueue_dequeue(self):
    queue = PriorityQueue()

    queue.enqueue("Елемент 1", 10)
    queue.enqueue("Елемент 2", 5)
    queue.enqueue("Елемент 3", 15)

    self.assertEqual(queue.dequeue(), "Елемент 3")
    self.assertEqual(queue.dequeue(), "Елемент 1")
    self.assertEqual(queue.dequeue(), "Елемент 2")
    self.assertTrue(queue.is_empty())



