class Solution:
    def jump(self, nums: List[int]) -> int:
        i = 0
        target = len(nums) - 1
        counter = 0
        idx = 0

        furthest = 0

        while idx < target:
            furthest = max(furthest, i + nums[i])

            if i == idx:
                counter += 1
                idx = furthest

                if idx >= target:
                    break

            i += 1

        return counter
