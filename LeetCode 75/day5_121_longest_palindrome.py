# Problem - https://leetcode.com/problems/longest-palindrome/


from collections import Counter


class Solution:
    def longestPalindrome(self, s: str) -> int:
        s_counter = Counter(s)

        palindrome_length = 0
        odd_length = False
        for char_count in s_counter.values():
            if char_count % 2 == 0:
                palindrome_length += char_count
            else:
                odd_length = True
                if char_count != 1:
                    palindrome_length += char_count - 1
        return palindrome_length if not odd_length else palindrome_length + 1


"""
Runtime: 42 ms, faster than 73.27% of Python3 online submissions for Longest Palindrome.
Memory Usage: 13.9 MB, less than 65.95% of Python3 online submissions for Longest Palindrome.
"""
