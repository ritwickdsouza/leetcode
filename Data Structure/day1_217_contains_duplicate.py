# Problem - https://leetcode.com/problems/contains-duplicate/


class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        return len(nums) > len(set(nums))


"""
Runtime: 836 ms, faster than 16.80% of Python3 online submissions for Contains Duplicate.
Memory Usage: 26 MB, less than 30.31% of Python3 online submissions for Contains Duplicate.
"""
