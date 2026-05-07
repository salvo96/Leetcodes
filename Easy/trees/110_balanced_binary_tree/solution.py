# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isBalanced(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        height = 0

        def computeHeight(root, height):
            if not root:
                return height, 0

            left_height, left_height_abs_diff = computeHeight(root.left, height)
            right_height, right_height_abs_diff = computeHeight(root.right, height)

            height_abs_diff = max(
                left_height_abs_diff,
                right_height_abs_diff,
                abs(left_height - right_height),
            )

            return max(left_height + 1, right_height + 1), height_abs_diff

        _, max_height_abs_diff = computeHeight(root, height)

        return max_height_abs_diff <= 1
