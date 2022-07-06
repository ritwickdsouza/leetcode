# Problem - https://leetcode.com/problems/intersection-of-two-arrays-ii/

from typing import List


from collections import Counter


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1_counter = Counter(nums1)
        nums2_counter = Counter(nums2)

        result = []
        for number in set([*nums1, *nums2]):
            intersection_count = min(
                nums2_counter[number], nums1_counter[number]
            )
            result.extend([number] * intersection_count)
        return result


"""
Runtime: 52 ms, faster than 89.52% of Python3 online submissions for Intersection of Two Arrays II.
Memory Usage: 14.1 MB, less than 51.97% of Python3 online submissions for Intersection of Two Arrays II.
"""
