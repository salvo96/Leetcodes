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

        def computeHeight(root):
            if not root:
                return 0, 0

            left_height, left_height_abs_diff = computeHeight(root.left)
            right_height, right_height_abs_diff = computeHeight(root.right)

            height_abs_diff = max(
                left_height_abs_diff,
                right_height_abs_diff,
                abs(left_height - right_height),
            )

            return max(left_height, right_height) + 1, height_abs_diff

        return computeHeight(root)[1] <= 1
