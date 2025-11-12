# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def visit_fill_dict(self, root):
        """
        In-order traversal
        """
        if root:
            self.visit_fill_dict(root.left)

            if self.prev and self.prev.val > root.val:
                if not self.first:
                    self.first = self.prev
                self.second = root
            self.prev = root

            self.visit_fill_dict(root.right)

    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        self.first = self.second = self.prev = None

        self.visit_fill_dict(root)

        self.first.val, self.second.val = self.second.val, self.first.val
