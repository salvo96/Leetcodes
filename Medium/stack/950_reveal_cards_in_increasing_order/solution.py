from collections import deque


class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        deck = sorted(deck, reverse=True)
        stack = deque()

        for elem in deck:
            if stack:
                tail = stack.pop()
                stack.appendleft(tail)
            stack.appendleft(elem)
        return list(stack)
