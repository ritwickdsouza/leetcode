# Problem - https://leetcode.com/problems/is-subsequence/


class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i, j = 0, 0
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
            j += 1
        return i == len(s)


"""
Runtime: 34 ms, faster than 91.15% of Python3 online submissions for Is Subsequence.
Memory Usage: 14 MB, less than 44.39% of Python3 online submissions for Is Subsequence.
"""
