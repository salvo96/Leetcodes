# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []

        if root:
            nodes = deque([root])

            while nodes:
                level = []
                for _ in range(len(nodes)):
                    node = nodes.popleft()
                    level.append(node.val)

                    if node.left:
                        nodes.append(node.left)
                    if node.right:
                        nodes.append(node.right)
                result.append(level)

        return result
