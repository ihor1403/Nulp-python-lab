import unittest
from src.rabin_karp import rabin_karp

class TestRabinKarp(unittest.TestCase):

    def test_single_match(self):
        haystack = "hello world"
        needle = "world"
        self.assertEqual(rabin_karp(haystack, needle), [6])

    def test_multiple_matches(self):
        haystack = "abababab"
        needle = "ab"
        self.assertEqual(rabin_karp(haystack, needle), [0, 2, 4, 6])

    def test_no_match(self):
        haystack = "abcdefg"
        needle = "xyz"
        self.assertEqual(rabin_karp(haystack, needle), [])

if __name__== '__main__':
    unittest.main()