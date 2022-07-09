# Problem - https://leetcode.com/problems/first-unique-character-in-a-string/


from collections import Counter


class Solution:
    def firstUniqChar(self, s: str) -> int:
        s_counter = Counter(s)

        for i, char in enumerate(s):
            if s_counter[char] == 1:
                return i
        return -1


"""
Runtime: 94 ms, faster than 92.22% of Python3 online submissions for First Unique Character in a String.
Memory Usage: 14.2 MB, less than 17.89% of Python3 online submissions for First Unique Character in a String.
"""
