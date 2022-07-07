# Problem - https://leetcode.com/problems/reshape-the-matrix/

from typing import List


def flatten(matrix: List[List[int]]) -> List[int]:
    return [i for j in matrix for i in j]


class Solution:
    def matrixReshape(
        self, mat: List[List[int]], r: int, c: int
    ) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        if m * n != r * c:
            return mat

        flat_mat = flatten(mat)
        return [[flat_mat.pop(0) for _ in range(c)] for _ in range(r)]


"""
Runtime: 99 ms, faster than 84.91% of Python3 online submissions for Reshape the Matrix.
Memory Usage: 14.5 MB, less than 98.75% of Python3 online submissions for Reshape the Matrix.
"""
