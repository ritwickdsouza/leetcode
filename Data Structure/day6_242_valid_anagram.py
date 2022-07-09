# Problem - https://leetcode.com/problems/valid-anagram/


from collections import Counter


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)


"""
Runtime: 76 ms, faster than 50.66% of Python3 online submissions for Valid Anagram.
Memory Usage: 14.5 MB, less than 34.55% of Python3 online submissions for Valid Anagram.
"""
