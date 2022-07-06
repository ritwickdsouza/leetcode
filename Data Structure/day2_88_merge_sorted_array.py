# Problem - https://leetcode.com/problems/merge-sorted-array/

from typing import List


class Solution:
    def merge(
        self, nums1: List[int], m: int, nums2: List[int], n: int
    ) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i, j, k = m - 1, n - 1, n + m - 1
        while j >= 0:
            if i >= 0 and nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1


"""
Runtime: 71 ms, faster than 19.69% of Python3 online submissions for Merge Sorted Array.
Memory Usage: 13.9 MB, less than 85.56% of Python3 online submissions for Merge Sorted Array.
"""
