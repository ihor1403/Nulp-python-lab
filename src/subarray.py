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

nums1 = [4, 5, 6]
nums2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(is_subarray(nums1, nums2))

nums1 = [1, 2, 3]
nums2 = [4, 5, 6, 7, 8, 9]
print(is_subarray(nums1, nums2))
