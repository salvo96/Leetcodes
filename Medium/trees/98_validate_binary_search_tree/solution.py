# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def checkBSTproperty(root, lower_bound, upper_bound):
            if not root:
                return True

            if not lower_bound < root.val < upper_bound:
                return False

            if not checkBSTproperty(root.left, lower_bound, root.val):
                return False

            return checkBSTproperty(root.right, root.val, upper_bound)

        return checkBSTproperty(root, float("-inf"), float("inf"))
