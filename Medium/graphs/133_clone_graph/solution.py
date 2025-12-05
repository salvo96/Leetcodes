"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional


class Solution:
    def dfs(self, node, cloned_dict=None):
        if not cloned_dict:
            cloned_dict = {}

        if node.val in cloned_dict.keys():
            return cloned_dict[node.val]

        cloned_node = Node(node.val, [])
        cloned_dict[node.val] = cloned_node

        for child in node.neighbors:
            child_node = self.dfs(child, cloned_dict)
            cloned_node.neighbors.append(child_node)
        return cloned_node

    def cloneGraph(self, node: Optional["Node"]) -> Optional["Node"]:
        if not node:
            return None
        return self.dfs(node)
