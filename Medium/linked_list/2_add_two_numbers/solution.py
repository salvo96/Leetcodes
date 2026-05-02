# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        last_node = ListNode()
        head = last_node

        remainder = 0
        while l1 or l2 or remainder > 0:
            node = ListNode()

            op1 = l1.val if l1 else 0
            op2 = l2.val if l2 else 0

            res = op1 + op2 + remainder
            node.val = res % 10
            remainder = res // 10

            last_node.next = node

            last_node = last_node.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return head.next
