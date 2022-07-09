# Problem - https://leetcode.com/problems/n-ary-tree-preorder-traversal/

from typing import List


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def preorder(self, root: Node) -> List[int]:
        result = []
        self.dfs(root, result)
        return result

    def dfs(self, node, result):
        if not node:
            return
        result.append(node.val)
        for child in node.children:
            self.dfs(child, result)


"""
Runtime: 93 ms, faster than 26.75% of Python3 online submissions for N-ary Tree Preorder Traversal.
Memory Usage: 16.3 MB, less than 48.46% of Python3 online submissions for N-ary Tree Preorder Traversal.
"""
