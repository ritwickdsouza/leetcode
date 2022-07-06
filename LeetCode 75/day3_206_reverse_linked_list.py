# Problem - https://leetcode.com/problems/reverse-linked-list/

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        previous = None
        current = head

        while current:
            next = current.next
            current.next = previous
            previous = current
            current = next
        return previous


"""
Runtime: 69 ms, faster than 20.25% of Python3 online submissions for Reverse Linked List.
Memory Usage: 15.3 MB, less than 93.96% of Python3 online submissions for Reverse Linked List.
"""
