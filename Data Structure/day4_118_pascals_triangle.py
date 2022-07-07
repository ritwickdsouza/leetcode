# Problem - https://leetcode.com/problems/pascals-triangle/

from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        result = [[1] * i for i in range(1, numRows + 1)]
        for i in range(numRows):
            for j in range(1, i):
                result[i][j] = result[i - 1][j - 1] + result[i - 1][j]
        return result


"""
Runtime: 48 ms, faster than 47.31% of Python3 online submissions for Pascal's Triangle.
Memory Usage: 14 MB, less than 17.80% of Python3 online submissions for Pascal's Triangle.
"""
