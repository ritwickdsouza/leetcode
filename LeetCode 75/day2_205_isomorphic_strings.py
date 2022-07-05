# Problem - https://leetcode.com/problems/isomorphic-strings/


class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        return len(set(zip(s, t))) == len(set(s)) == len(set(t))


"""
Runtime: 61 ms, faster than 58.03% of Python3 online submissions for Isomorphic Strings.
Memory Usage: 14.1 MB, less than 89.00% of Python3 online submissions for Isomorphic Strings.
"""
