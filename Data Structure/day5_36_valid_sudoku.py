# Problem - https://leetcode.com/problems/valid-sudoku/

from typing import List

import itertools


class Solution:
    def checkUnique(self, nums: List[str]) -> bool:
        return len(nums) == len(set(nums))

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            row = [num for num in board[i] if num != '.']
            if not self.checkUnique(row):
                return False

        for i in range(9):
            column = [row[i] for row in board if row[i] != '.']
            if not self.checkUnique(column):
                return False

        for i, j in list(itertools.product(range(0, 9, 3), range(0, 9, 3))):
            sub_box = []
            for n, m in list(itertools.product(range(0, 3), range(0, 3))):
                sub_box.append(board[i + n][j + m])
            sub_box = [num for num in sub_box if num != '.']
            if not self.checkUnique(sub_box):
                return False

        return True


"""
Runtime: 125 ms, faster than 68.32% of Python3 online submissions for Valid Sudoku.
Memory Usage: 14 MB, less than 34.76% of Python3 online submissions for Valid Sudoku.
"""
