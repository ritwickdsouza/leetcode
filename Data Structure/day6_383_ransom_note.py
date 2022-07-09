# Problem - https://leetcode.com/problems/ransom-note/


from collections import Counter


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransom_note_counter = Counter(ransomNote)
        magazine_counter = Counter(magazine)

        for char, count in ransom_note_counter.items():
            if not magazine_counter[char] >= count:
                return False
        return True


"""
Runtime: 92 ms, faster than 48.20% of Python3 online submissions for Ransom Note.
Memory Usage: 14.1 MB, less than 94.03% of Python3 online submissions for Ransom Note.
"""
