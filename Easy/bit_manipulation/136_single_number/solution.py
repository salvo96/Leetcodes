class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result = nums[0]

        for idx in range(1, len(nums)):
            result ^= nums[idx]

        return result
