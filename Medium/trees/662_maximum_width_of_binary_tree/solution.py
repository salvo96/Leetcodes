# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque


class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        level_nodes = deque([(root, 0)])
        max_width = 0

        while level_nodes:
            level_len = len(level_nodes)

            level_counter = level_nodes[-1][1] - level_nodes[0][1] + 1
            max_width = max(max_width, level_counter)

            for _ in range(level_len):
                node, node_idx = level_nodes.popleft()

                if node.left:
                    level_nodes.append((node.left, node_idx * 2))

                if node.right:
                    level_nodes.append((node.right, node_idx * 2 + 1))

        return max_width
