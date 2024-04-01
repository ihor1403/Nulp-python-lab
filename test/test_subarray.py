import unittest

def is_subarray(nums1, nums2):
    if not nums1:
        return True
    if not nums2:
        return False
    i = 0
    for num in nums2:
        if num == nums1[i]:
            i += 1
        if i == len(nums1):
            return True
    return False

if __name__ == '__main__':
    unittest.main()

class TestIsSubarray(unittest.TestCase):
    def test_example_1(self):
        nums1 = [1, 2, 3]
        nums2 = [1, 2, 3, 4]
        self.assertTrue(is_subarray(nums1, nums2))

    def test_example_2(self):
        nums1 = [4, 2]
        nums2 = [1, 2, 3, 4]
        self.assertFalse(is_subarray(nums1, nums2))

    def test_example_3(self):
        nums1 = [1, 3, 5]
        nums2 = [1, 2, 3, 4, 5]
        self.assertTrue(is_subarray(nums1, nums2))


