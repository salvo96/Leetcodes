# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def computeDiameter(node):
            if not node:
                return 0, 0

            max_len_left, diam_left = computeDiameter(node.left)
            max_len_right, diam_right = computeDiameter(node.right)

            return max(max_len_left, max_len_right) + 1, max(
                diam_left, diam_right, max_len_left + max_len_right
            )

        return computeDiameter(root)[1]
