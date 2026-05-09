# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        output = []

        if not root:
            return output

        nodes = deque([root])

        while nodes:
            level_size = len(nodes)

            for i in range(level_size):
                node = nodes.popleft()

                if i == 0:
                    output.append(node.val)

                if node.right:
                    nodes.append(node.right)
                if node.left:
                    nodes.append(node.left)

        return output
