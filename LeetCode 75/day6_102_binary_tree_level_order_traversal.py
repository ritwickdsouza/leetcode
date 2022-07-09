# Problem - https://leetcode.com/problems/binary-tree-level-order-traversal/

from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        result = []
        current_level = [root]
        while len(current_level):
            result.append([node.val for node in current_level if node])
            next_level = []
            for node in current_level:
                if node and node.left:
                    next_level.append(node.left)
                if node and node.right:
                    next_level.append(node.right)
            current_level = next_level
        return result


"""
Runtime: 67 ms, faster than 19.77% of Python3 online submissions for Binary Tree Level Order Traversal.
Memory Usage: 14.1 MB, less than 84.09% of Python3 online submissions for Binary Tree Level Order Traversal.
"""
