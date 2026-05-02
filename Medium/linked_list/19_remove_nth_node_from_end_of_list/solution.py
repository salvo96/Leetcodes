# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
################################################################## Iterative Solution ##################################################################
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        counter = 0

        node = head
        while node:
            counter += 1
            node = node.next

        if counter == n:
            return head.next

        node = head
        while node:
            counter -= 1
            if counter == n:
                node.next = node.next.next
                return head
            node = node.next


################################################################## Recursive Solution ##################################################################
class Solution:
    def __init__(
        self,
    ):
        self.counter = 0

    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head.next:
            head.next = self.removeNthFromEnd(head.next, n)

        self.counter += 1

        if self.counter == n:
            return head.next

        return head
