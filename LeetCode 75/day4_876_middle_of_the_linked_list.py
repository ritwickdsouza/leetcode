# Problem - https://leetcode.com/problems/middle-of-the-linked-list/

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        x = head
        y = head
        while x and x.next:
            x = x.next.next
            y = y.next
        return y


"""
Runtime: 61 ms, faster than 15.18% of Python3 online submissions for Middle of the Linked List.
Memory Usage: 13.8 MB, less than 55.35% of Python3 online submissions for Middle of the Linked List.
"""
