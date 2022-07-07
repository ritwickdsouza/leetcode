# Problem - https://leetcode.com/problems/linked-list-cycle-ii/

from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        pointer = head
        seen_nodes = []
        while pointer:
            if pointer in seen_nodes:
                return pointer
            seen_nodes.append(pointer)
            pointer = pointer.next
        return None


"""
Runtime: 1644 ms, faster than 5.02% of Python3 online submissions for Linked List Cycle II.
Memory Usage: 17.3 MB, less than 94.45% of Python3 online submissions for Linked List Cycle II.
"""
