# Problem - https://leetcode.com/problems/find-pivot-index/

from typing import List


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total_sum = sum(nums)
        left_sum = 0
        right_sum = total_sum
        for i, num in enumerate(nums):
            right_sum -= num
            if left_sum == right_sum:
                return i
            left_sum += num
        return -1


"""
Runtime: 149 ms, faster than 98.15% of Python3 online submissions for Find Pivot Index.
Memory Usage: 15.2 MB, less than 48.98% of Python3 online submissions for Find Pivot Index.
"""
