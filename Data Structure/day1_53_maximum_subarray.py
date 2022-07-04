# Problem - https://leetcode.com/problems/maximum-subarray/


class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        current_sum = 0
        max_sum = float('-inf')
        for num in nums:
            current_sum = max(num, current_sum + num)
            max_sum = max(max_sum, current_sum)
        return max_sum if nums else 0


"""
Runtime: 1393 ms, faster than 15.80% of Python3 online submissions for Maximum Subarray.
Memory Usage: 27.9 MB, less than 38.98% of Python3 online submissions for Maximum Subarray.
"""
