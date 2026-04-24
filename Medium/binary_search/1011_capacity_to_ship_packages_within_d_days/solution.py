class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        max_weights = range(max(weights), sum(weights) + 1)

        left, right = 0, len(max_weights) - 1
        while left < right:
            middle = (left + right) // 2
            days_counter = 1

            tot_weight = 0
            for weight in weights:
                tot_weight += weight
                if tot_weight > max_weights[middle]:
                    days_counter += 1
                    tot_weight = weight

            if days >= days_counter:
                right = middle
            else:
                left = middle + 1
        return max_weights[left]
