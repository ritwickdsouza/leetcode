# Problem - https://leetcode.com/problems/two-sum/

from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, num in enumerate(nums):
            other_num = target - num
            if other_num in seen:
                return [i, seen[other_num]]
            else:
                seen[num] = i
        return [-1, -1]


"""
Runtime: 137 ms, faster than 38.30% of Python3 online submissions for Two Sum.
Memory Usage: 15.1 MB, less than 50.16% of Python3 online submissions for Two Sum.
"""
