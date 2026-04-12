class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()

        left, right = 0, len(people) - 1

        output = 0
        while left <= right:
            if limit >= people[left] + people[right]:
                left += 1

            right -= 1
            output += 1

        return output
