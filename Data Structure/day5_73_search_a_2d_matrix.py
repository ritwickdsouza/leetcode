# Problem - https://leetcode.com/problems/search-a-2d-matrix/

from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, columns = len(matrix), len(matrix[0])
        low, high = 0, rows * columns - 1
        print(matrix, target)
        while high >= low:
            mid = (low + high) // 2
            num = matrix[mid // columns][mid % columns]

            if num == target:
                return True
            elif num < target:
                low = mid + 1
            else:
                high = mid - 1
        return False


"""
Runtime: 71 ms, faster than 44.67% of Python3 online submissions for Search a 2D Matrix.
Memory Usage: 14.5 MB, less than 7.75% of Python3 online submissions for Search a 2D Matrix.
"""
