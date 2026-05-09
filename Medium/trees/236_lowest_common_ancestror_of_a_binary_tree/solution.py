# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def lowestCommonAncestor(
        self, root: "TreeNode", p: "TreeNode", q: "TreeNode"
    ) -> "TreeNode":
        p_ancestror, q_ancestror = None, None

        def findAncestror(root, p, q):
            nonlocal p_ancestror, q_ancestror

            if not root:
                return root

            if root == p:
                p_ancestror = root
            if root == q:
                q_ancestror = root

            left_child = findAncestror(root.left, p, q)
            right_child = findAncestror(root.right, p, q)

            if p_ancestror == q_ancestror and p_ancestror:
                return p_ancestror

            if p_ancestror is not None and (
                p_ancestror == left_child or p_ancestror == right_child
            ):
                p_ancestror = root

            if q_ancestror is not None and (
                q_ancestror == left_child or q_ancestror == right_child
            ):
                q_ancestror = root

            return root

        return findAncestror(root, p, q)
