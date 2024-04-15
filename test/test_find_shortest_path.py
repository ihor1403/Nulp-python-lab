import unittest
from lab7 import find_shortest_path

class TestShortestPath(unittest.TestCase):

  def test_blocked_maze(self):
    maze = [
      [0, 0, 0, 0, 0],
      [0, 0, 1, 0, 0],
      [0, 0, 1, 0, 0],
      [0, 1, 1, 1, 0],
      [0, 0, 0, 0, 0]
    ]
    start = (2, 1)
    end = (4, 3)
    expected_path = []
    self.assertEqual(find_shortest_path(maze, start, end), expected_path)

if __name__ == "__main__":
  unittest.main()
