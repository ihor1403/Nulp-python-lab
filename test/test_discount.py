import unittest
from lab2 import total_with_discount


class TestTotalWithDiscount(unittest.TestCase):

  def test_example1(self):
    prices = [100, 200, 300, 400, 500]
    expected = 1380.00
    actual = total_with_discount(prices)
    self.assertEqual(expected, actual)

  def test_example2(self):
    prices = [50, 100, 150, 200]
    expected = 440.00
    actual = total_with_discount(prices)
    self.assertEqual(expected, actual)


if __name__ == '__main__':
  unittest.main()