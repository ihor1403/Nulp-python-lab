import unittest
from find_shortest_path import find_shortest_path

class TestFindShortestPath(unittest.TestCase):
    def test_shortest_path_found(self):
        maze = [
            [1, 1, 1, 1],
            [1, 0, 0, 1],
            [1, 1, 1, 1],
        ]
        start = (0, 0)
        end = (2, 3)

        expected_path = [(0, 0), (0, 1), (1, 0), (0, 2), (2, 0), (0, 3), (2, 1), (1, 3), (2, 2), (2, 3)]

        result = find_shortest_path(maze, start, end)
        self.assertEqual(result, expected_path)

    def test_no_path_found(self):
        maze = [
            [1, 0, 1],
            [1, 0, 1],
            [1, 0, 1],
        ]
        start = (0, 0)
        end = (2, 2)

        result = find_shortest_path(maze, start, end)
        self.assertEqual(result, [])

if __name__ == "__main__":
    unittest.main()
