import unittest
from collections import defaultdict

from lab6 import get_optimal_order


class TestOptimalOrder(unittest.TestCase):

    def test_empty_dependencies(self):
        dependencies = {}
        order = get_optimal_order(dependencies)
        self.assertEqual(order, [])

    def test_single_doc(self):
        dependencies = defaultdict(list)
        dependencies["doc1"] = []
        order = get_optimal_order(dependencies)
        self.assertEqual(order, ["doc1"])


    def test_cycle_detection(self):
        dependencies = defaultdict(list)
        dependencies["doc1"] = ["doc2"]
        dependencies["doc2"] = ["doc1"]
        with self.assertRaises(Exception):
            get_optimal_order(dependencies)


if __name__ == "__main__":
    unittest.main()