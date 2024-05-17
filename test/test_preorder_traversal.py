import unittest
from src.preorder_traversal import pre_order_traversal, BinaryTree

class TestPreOrderTraversal(unittest.TestCase):
    def test_pre_order_traversal(self):
        root = BinaryTree(1)
        root.left = BinaryTree(2)
        root.right = BinaryTree(3)
        root.left.left = BinaryTree(4)
        root.left.right = BinaryTree(5)

        expected_result = [1, 2, 4, 5, 3]

        result = pre_order_traversal(root)


        self.assertEqual(result, expected_result)

if __name__ == '__main__':
    unittest.main()
