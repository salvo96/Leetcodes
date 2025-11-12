import math


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        i = 0
        j = max(piles) - 1
        pointer = (i + j) // 2

        while i <= j:
            hours_count = 0
            for val in piles:
                hours_count += math.ceil(val / (pointer + 1))
            if hours_count <= h:  # I have to eat slower
                j = pointer - 1
            else:  # I have to eat faster
                i = pointer + 1
            pointer = (i + j) // 2
        return i + 1
