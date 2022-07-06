# Problem - https://leetcode.com/problems/running-sum-of-1d-array/

from typing import List


class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        running_sum = 0
        running_sums = []
        for num in nums:
            running_sum += num
            running_sums.append(running_sum)
        return running_sums


"""
Runtime: 47 ms, faster than 81.73% of Python3 online submissions for Running Sum of 1d Array.
Memory Usage: 14.1 MB, less than 70.74% of Python3 online submissions for Running Sum of 1d Array.
"""
