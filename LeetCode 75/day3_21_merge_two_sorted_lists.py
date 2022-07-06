# Problem - https://leetcode.com/problems/merge-two-sorted-lists/

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        dummy = current = ListNode()
        while list1 and list2:
            if list1.val < list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next
        current.next = list1 or list2
        return dummy.next


"""
Runtime: 73 ms, faster than 17.77% of Python3 online submissions for Merge Two Sorted Lists.
Memory Usage: 13.9 MB, less than 79.01% of Python3 online submissions for Merge Two Sorted Lists.
"""
